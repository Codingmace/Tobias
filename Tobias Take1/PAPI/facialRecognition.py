import face_recognition
import cv2
import numpy as np
import os

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)

def getImageEncoding(path):
    people = os.listdir(path)
    faces = []
    encodings = []
    for p in people:
        faces.append(path + p + "/Face/")
    for f in faces:
        faceList = os.listdir(f)
        tempImage = face_recognition.load_image_file(f + faceList[0])
        tempEncoding = face_recognition.face_encodings(tempImage)[0]
        encodings.append(tempEncoding)
    return encodings

def getNames(basePath):
    return os.listdir(basePath)
    
def facialRecognition():
    video_capture = cv2.VideoCapture(0)
    knownFaceNames = getNames("./User/")
    knownFaceEncodings = getImageEncoding("./User/") # Is an array
    # Initialize some variables
    faceLocations = []
    faceEncodings = []
    faceNames = []
    processFrame = True 
    unknownsCount = 0
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        smallFrame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = smallFrame[:, :, ::-1]

        # Only process every other frame of video to save time
        if processFrame:
            # Find all the faces and face encodings in the current frame of video
            faceLocations = face_recognition.face_locations(rgb_small_frame)
            faceEncodings = face_recognition.face_encodings(rgb_small_frame, faceLocations)

            faceNames = []
            for faceEncoding in faceEncodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(knownFaceEncodings, faceEncoding)
                name = "Unknown"

                # Or instead, use the known face with the smallest distance to the new face
                faceDistances = face_recognition.face_distance(knownFaceEncodings, faceEncoding)
                bestMatchIndex = np.argmin(faceDistances)
                if matches[bestMatchIndex]:
                    name = knownFaceNames[bestMatchIndex]
                    return name
                if name == "Unknown":
                    unknownsCount += 1

                if unknownsCount >= 6: # Limit before return false
                    cv2.imwrite("./User/image.jpg" , frame) # Writting the image
                    return name
                print(name)
                faceNames.append(name)

        processFrame = not processFrame



        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


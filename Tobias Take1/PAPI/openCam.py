import webbrowser

def openCamera(state):
    f = open("Data/stateMap.txt", "r")
    lines = f.readlines()
    stateList = []
    linkList = []
    for line in lines:
        split = line.split(" - ")
        stateList.append(split[0].strip().lower())
        linkList.append(split[1].strip())
    print(stateList)
    if state in stateList:
        ind = stateList.index(state)
        return linkList[ind]
    else:
        return "NONE"


def findWebCamera(state):
    state = state.lower()
    cameraLink = openCamera(state)
    if "NONE" in cameraLink:
        return state + " is not a valid state"
    else:
        webbrowser.open(cameraLink)
        print(cameraLink)
        return "I have opened up " + state + " cameras"


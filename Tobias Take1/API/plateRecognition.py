import requests
from API.variables import rapidApiKey

def recognizeByUrl(imageUrl):
    url = "https://number-plate-recognition.p.rapidapi.com/recognition"

    payload = "image_url=" + imageUrl
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "number-plate-recognition.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

# Binary Image? Maybe?
def recognizeByImage(fileData):
# Binary Imagex
    url = "https://number-plate-recognition.p.rapidapi.com/recognition"
    
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "number-plate-recognition.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

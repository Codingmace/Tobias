import requests
from API.variables import rapidApiKey

def transcribeUrl(audioUrl):
    url = "https://transcribe.p.rapidapi.com/api/v1/transcribe_url/"

    payload = "{\r\n    \"url\": " + audioUrl + "\r\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response


def getTask(taskID):
    url = "https://transcribe.p.rapidapi.com/api/v1/tasks/" + taskID

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response

def serviceStatus():
    url = "https://transcribe.p.rapidapi.com/api/v1/"

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response

def getTasks():
    url = "https://transcribe.p.rapidapi.com/api/v1/tasks/"

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response

## Import Binary? audio local file?
def transcribe(fileData):
    url = "https://transcribe.p.rapidapi.com/api/v1/transcribe/"

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

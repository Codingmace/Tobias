import requests
from API.variables import rapidApiKey

def OImage2Text(imageUrl, filename):
    url = "https://ocrly-image-to-text.p.rapidapi.com/"

    querystring = {"imageurl": imageUrl,"filename": filename}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "ocrly-image-to-text.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

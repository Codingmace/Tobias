import requests
from API.variables import rapidApiKey

def downloadVideo(videoId):
    url = "https://youtube-to-mp32.p.rapidapi.com/yt_to_mp3"

    querystring = {"video_id":videoId}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "youtube-to-mp32.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

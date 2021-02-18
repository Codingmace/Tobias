import requests
from API.variables import rapidApiKey

def defineWord(word):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term" : word}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response

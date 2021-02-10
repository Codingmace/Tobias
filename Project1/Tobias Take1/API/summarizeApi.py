import requests
from API.variables import rapidApiKey

def summarize(url):
    baseUrl = "https://summarization3.p.rapidapi.com/summary/v1/"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "summarization3.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response

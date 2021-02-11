import requests
from API.variables import rapidApiKey

def fetchText(url):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/text"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response

def pos(url):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/pos"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response


def namedEntity(url):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/ner"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response

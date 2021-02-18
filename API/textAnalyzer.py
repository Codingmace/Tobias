import requests
from API.variables import rapidApiKey

def contentExtract(url):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/text"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response


def namedExtract(url):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/ner"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response


def partOfSpeech(url):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/pos"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response

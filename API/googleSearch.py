import requests
from API.variables import rapidApiKey

def search(term, number):
    url = "https://google-search3.p.rapidapi.com/api/v1/search/q=" + term + "&num="+ str(number)
    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response


def images(term):
    url = "https://google-search3.p.rapidapi.com/api/v1/images/q=" + term
    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response


def crawl(term, number):
    url = "https://google-search3.p.rapidapi.com/api/v1/crawl/q=" + term + "&num=" + str(number)
    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response


def news(term):
    url = "https://google-search3.p.rapidapi.com/api/v1/news/q=" + term
    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response



def SERP(payload):
    # THIs is a post request and very tricky

    url = "https://google-search3.p.rapidapi.com/api/v1/serp/"

    payload = "{\r\n    \"query\": \"q=google+search+api&num=100\",\r\n    \"website\": \"https://rapidapi.com\"\r\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

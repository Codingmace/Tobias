import requests
import json
from API.variables import rapidApiKey

def ipWorldWide(apiKey):
    url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"

    querystring = {"apikey": apiKey}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dataResponse = response.json()

    # Needed Data
    neededData = ['zipCode', 'accuracyRadius','city','timezone','latitude','longitude','ip','stateCode','status']
    importantData = []

    for data in neededData:
        importantData.append(dataResponse[data])

    print(neededData)
    print(importantData)
    return response

    """zipCode = data['zipCode']
    radius = data['accuracyRadius']



    {"zipCode":"75071"
    "accuracyRadius":10
    "city":"McKinney"
    "timezone":"America/Chicago"
    "latitude":33.1974
    "longitude":-96.6177
    "ip":"45.16.197.205"
    "stateCode":"TX"
    "status":200}
    """

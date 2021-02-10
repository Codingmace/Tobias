import requests
from API.variables import rapidApiKey

def ip2location(ipAddress,apiKey):
    url = "https://ip2location-ip2location-v1.p.rapidapi.com/"

    querystring = {"ip": ipAddress,"key": apiKey,"package": "WS9"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "ip2location-ip2location-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

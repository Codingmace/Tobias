import requests
from API.variables import rapidApiKey

def verifyPhone(number):
    url = "https://veriphone.p.rapidapi.com/verify"

    querystring = {"phone":number,"default_country":"US"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "veriphone.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

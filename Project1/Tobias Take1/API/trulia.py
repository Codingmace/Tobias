import requests
from API.variables import rapidApiKey

def searching(city, state, pageNum):
    url = "https://trulia1.p.rapidapi.com/search"
    city = "new%20york" # URL Encoding
    payload = "city="+ city+"&state_code=" + state + "&page=" + str(pageNum)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "trulia1.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response


def propertyDetail():
    url = "https://trulia1.p.rapidapi.com/property"

    payload = "property_url=https%3A%2F%2Fwww.trulia.com%2Fp%2Fny%2Fnew-york%2F150-central-park-s-new-york-ny-10019--689699"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "trulia1.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

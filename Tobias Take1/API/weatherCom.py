import requests
from API.variables import rapidApiKey

def covid19(language):
    url = "https://weather-com.p.rapidapi.com/v3/wx/disease/tracker/countryList/current"

    querystring = {"language": language}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def forecastDaily(geocode, units, lang): 
    url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/daily/3day"

    querystring = {"geocode":geocode,"units":units,"language":lang}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def forecastHourly(geocode, units, lang):
    url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/hourly/1day"

    querystring = {"geocode":geocode,"units":units,"language":lang}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def historical30d(geocode, units, lang):
    url = "https://weather-com.p.rapidapi.com/v3/wx/conditions/historical/dailysummary/30day"

    querystring = {"geocode":geocode,"units":units,"language":lang}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response



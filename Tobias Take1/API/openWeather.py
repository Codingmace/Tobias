import requests
from API.variables import rapidApiKey

def currentWeather(location, latitude, longitude, callback, lang, unit, mode): #D Dont know what to do with ID
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":location,"lat":latitude,"lon":longitude,"callback":callback,"id":"2172797","lang":lang,"units":units,"mode":mode}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def forecast(location, latitude, longitude, count, units, mode, lang):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q":location,"lat":latitude,"lon":longitude,"cnt":count,"units":units,"mode":mode,"lang":lang}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def searchWeatherData(location, latitude, longitude, count, mode, types, units):
    url = "https://community-open-weather-map.p.rapidapi.com/find"

    querystring = {"q":location,"cnt":count,"mode":mode,"lon":longitude,"type":types,"lat":latitude,"units":units}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def historicalWeather(latitude, longitude):
    url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

    querystring = {"lat":latitude,"lon":longitude,"dt":"1590094153"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def climateForecast30(city):
    url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

    querystring = {"q": city}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def forecast5d3h(location, latitude, longitude, lang, count, zipcode):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"q":location,"lat":latitude,"lon":longitude,"lang":lang,"cnt":count,"zip":zipcode}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

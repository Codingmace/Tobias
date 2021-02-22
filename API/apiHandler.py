## This is to help with importing the API only when needed
import sys
import json
from API.variables import weatherInfo
from IPAddress import getMyIPv4Address, getMyIPv6Address

#sys.path.append("API/")
def readData(filename):
    f = open(filename, "rb")
    fin = f.readline()
    lines = f.readlines()
    for line in lines:
        fin += line
    return fin

def removingJson(jsonData, removingList):
    for l in removingList:
        del jsonData[jsonData.get(l)]
    return jsonData

def refineJson(jsonData, addList):
    newJson = json.dump("")
    for l in addList:
        newJson.update(jsonData.get(l))
    return newJson


####################
# Urban Dictionary #
# To define words  #
####################
def wordDefinition(word):
    from API.urbanDictionary import defineWord
    dataResponse = defineWord(word).json()
    return dataResponse['list'][0]['definition'] # First word definition
# Possible improvements : Go through the list and choose the best one. Display all of them


# Encoding for the google
def googleEncode(term):
    return term.replace("+", "%2B").replace(" ", "+")


# Google Search : Look up things on google
def google(query):
    from API.googleSearch import search, images, crawl, news
    if "search" in query:
        query = query.replace("search ","")
        resultCount = 10
        split = query.split(" ")
        lastResult = split[-1]
        if(lastResult.isdigit()):
            resultCount = int(lastResult)
            query = query.replace(lastResult,"")
        return search(googleEncode(query), resultCount)
        # So much can be done with this
    elif "image" in query:
        query = query.replace("image ","")
        return images(googleEncode(query))
        # Show the images Maybe
    elif "crawl" in query:
        query = query.replace("crawl","")
        resultCount = 10
        split = query.split(" ")
        lastResult = split[-1]
        if(lastResult.isdigit()):
            resultCount = int(lastResult)
            query = query.replace(lastResult,"")
        return crawl(googleEncode(query), resultCount)
    elif "news" in query:
        query = query.replace("news","")
        return news(googleEncode(query))

# Revese Image : Google Reverse Image Search
def reverseImageSearch(query):
    from API.reverseImage import reverseImage
    imageUrl = query # Modify for the actual file URL
    results = reverseImage(imageUrl)
    return results
#    return results.json()['googleSearchResult']



##########################
# Open Proxy             #
# Reports all open       #
# proxies at that moment #
##########################
def proxyCheck():
    from API.openProxies import openProxy
    return openProxy().text


##################################
# Cat Facts                      #
# Returns random cat fact        #
# with optional Length parameter #
##################################
def randomCatFact(query):
    from API.catFacts import catFact
    length = -1
    if "random" not in query:
        try:
            temp = int(query.strip())
            length = temp
        except:
            length = -1
    return catFact(length).json()['data'][0]['fact']


# Open Weather : Reports back the weather
""" NEEDS: have to sort out how I am going to do location """
def openWeather(query):
    from API.openWeather import currentWeather, forecast, searchWeatherData, historicalWeather, climateForecast30, forecast5d3h
    from API.ipGeoLocation import ipLocation
    ipv4 = getMyIPv4Address()
    callback = weatherInfo['callback']
    mode = weatherInfo['mode']
    types = weatherInfo['types']
    measurement = weatherInfo['measurement']
    units = weatherInfo['units']
    lang = weatherInfo['lang']
    count = weatherInfo['count']
    geoInfo1 = ipLocation(ipv4)
    geoInfo = geoInfo1.json()
#    print(geoInfo)
    latitude = geoInfo['latitude']
    longitude = geoInfo['longitude']
    city = geoInfo['city']
    country = geoInfo['country']['code']
    location = city + "," + country
    # Location example San francisco,us
    if "current weather" in query:
        return currentWeather(location, latitude, longitude, callback, lang, units, mode)
    elif "forecast today" in query:
        return forecast(location, latitude, longitude, count, units, mode, lang)
    elif "search" in query:
        return searchWeatherData(location, latitude, longitude, count, mode, types, units)
    elif "historical data" in query:
        return historicalWeather(latitude, longitude)
    elif "climate forecast" in query:
        return climateForecast30(city)
    elif "5 day forecast" in query:
        # Have to redo because maybe another spot and don't want mixed data.
        from API.ip2Location import ip2location
        geoInfo1 = ip2location(ipv4, "demo")
        geoInfo = geoInfo.json()
        latitude = geoInfo['latitude']
        longitude = geoInfo['longitude']
        city = geoInfo['city_name']
        country = geoInfo['country_code']
        zipcode = geoInfo['zipcode']
        location = city + "," + country
        return forecast5d3h(location, latitude, longitude, lang, count, zipcode)
    else:
        print("That is not a valid one")
        return ""

# Weather.com : Reports back weather
def weather(query):
    from API.weatherCom import covid19, forecastDaily, forecastHourly, historical30d
    currentWeather = weatherInfo
    language = weatherInfo['language']
    if "covid" in query:
        query = query.replace("covid","")
        response = covid19(language)
        result = response.json()['covid19']
        needed = ['recordLocation', 'totalPopulation','confirmed','deaths','dateReport','dateReportUtc']
        result = refineJson(result,needed)
        if (query in result['recordedLocation']) and not(query == ""):
            ind = result['recordedLocation'][query]
            tot = ""
            for i in needed:
                tot += result[i][ind] + " "
            return tot
        else:
            population= 0 # Population
            conf = 0 # Confirmed
            dea = 0 # deaths
            tot = "World population: "
            for a in result['totalPopulation']:
                population += int(a)
            for b in result['confirmed']:
                conf += int(b)
            for c in result['deaths']:
                dea += int(c)
            return tot + " " + str(population) + " " + str(conf) + " " + str(dea)

    lang = weatherInfo['lang']
    geocode = "100, 20" # Get this from somewhere else
    units = weatherInfo['units']
    if "daily forecast" in query:
        return forecastDaily(geocode, units, lang)
    elif "hourly forecast" in query:
        return forecastHourly(geocode, units, lang)
    elif "historical records" in query:
        return historical30d(geocode, units, lang)
    else:
        x = openWeather(query)
        return x
#        return openWeather(query)

#####################
# Email Validate    #
# Check if email    #
# is valid or not   #
#####################
def validateEmailAddress(query):
    from API.emailValidate import validEmail
    result = validEmail(query).json()
    dispose = result['disposable'] == 'true'
    valid = result['valid'] == 'true'
    fin = ""
    if not valid:
        fin += "non"
    fin += "valid "
    if not dispose:
        fin += "non"
    fin += "disposable email"
    return fin


##############################
# Verifone                   #
# Verifies if a phone is     #
# valid (Default Country US) #
##############################
def verifyPhoneNumber(query):
    from API.veriphone import verifyPhone
    response = verifyPhone(query)
    result = response.json()
    if result['phone_valid'] == True:
        return "valid phone with type : " + result['phone_type']  +" and carrier : " + result['carrier']
    else:
        return "That phone is not valid"


# Transcribe : Turns audio into text
def transcribeAudio(query):
    from API.transcribe import transcribeUrl, getTask, serviceStatus, getTasks, transcribe
    if "url" in query:
        query = query.replace("url", "")
        return transcribeUrl(query)
    elif "get task" in query:
        query = query.replace("get task" , "")
        return getTask()
    elif "status" in query:
        return serviceStatus()
    elif "tasks" in query:
        return getTasks()
    elif "file" in query:
        query = query.replace("file","")
        fileData = readData(query)
        return transcribe(fileData)
    else:
        return ""

def encode(term): # URL Encoding
    return term.replace(" ", "%20")

# Text Analyzer : Analyzes the contents of a URL
def analyzeUrlText(query):
    from API.textAnalyzer import contentExtract, namedExtract, partOfSpeech
    if "content" in query:
        query = query.replace("content", "")
        return contentExtract(query)
    elif "named" in query:
        query= query.replace("named","")
        return namedExtract(query)
    elif "part of speech" in query:
        query = query.replace("part of speech", "")
        return partOfSpeech(query)
    else:
        return ""

# Test : To grab text, identify parts of speech, identify name of entities
def analyzeText(query):
    from API.testTextHelp import fetchText, namedEntity, pos
    if "fetch" in query:
        query = query.replace("fetch", "")
        return fetchText(query)
    elif "named" in query:
        query= query.replace("named","")
        return namedEntity(query)
    elif "part of speech" in query:
        query = query.replace("part of speech", "")
        return pos(query)
    else:
        return ""

# Summarize API : Summarize the text of a URL link
def summarizeUrlText(query):
    from API.summarizeApi import summarize
    return summarize(query)

# OCRLY : URL Image to text
def urlImage2Text(query): # Uses true url encoding
    from API.OCRLY import OImage2Text
    split = query.split(" ")
    if len(split) == 2:
        return OImage2Text(split[0], split[1])
    else:
        return OImage2Text(split[0], "testFilename.txt")


####################
# Youtube Download #
# Download Youtube #
# Video by VideoID #
####################
def downloadYoutube(query):
    from API.youtubeDownload import downloadVideo
    response = downloadVideo(query)
    result = response.json()
    if result['Status'] == "Success":
        return result['Download_url']
    else:
        return "I have failed to get a URL"


# Threat Detect :
def detectUrlThreats(query):
    from API.threatDetector import detectThreat
    print("if url must translate to an ip address")
    print("If Ip address don't need to do anything which is the basis")
    return detectThreat(query)

# URL Intel : Extracts Links from a URL
def IntelligentUrl(query):
    from API.urlIntel import urlIntel
    return urlIntel(query)


#########################
# IP2Location           #
# Turn Ip into location #
#########################
def ip2Location(query):
    from API.ip2Location import ip2location
    response = ip2location(query, "demo")
    result = response.json()
    print("Longitude : " + result['longitude'] + "\nLatitude : " + result['latitude'])
    return result['city_name'] + " " + result['region_name'] + " zipcode " + result['zip_code']

# Find any Ip address world wide : IPv6 and IPv4
def ipLocWW(query):
    from API.ipWorldWide import ipWorldWide
    return ipWorldWide(query) # Not sure if this one will work

# IP Geolocation Web Service : IP Geolocate
def ipGeoLocate(query):
    from API.ipGeoLocation import ipLocation
    return ipLocation(query)

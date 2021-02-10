import requests
from API.variables import rapidApiKey

def ipLocation(ipAddress):
    url = "https://ip-location5.p.rapidapi.com/get_geo_info"

    payload = "ip="+ipAddress
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "ip-location5.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    dataResponse = response.json()

    # print(response.text)

    neededData = ['ip','region','city','latitude','longitude']
    importantData = []

    for data in neededData:
        importantData.append(dataResponse[data])

#    print(neededData)
#    print(importantData)
    return response

    """
    {
    "ip":"45.16.197.205"
    "continent":{2 items
    "code":"NA"
    "name":"North America"
    }
    "country":{5 items
    "code":"US"
    "name":"United States"
    "capital":"Washington"
    "currency":"USD"
    "phone-code":"1"
    }
    "region":"Texas"
    "city":"Richardson"
    "latitude":32.9483
    "longitude":-96.7299
    }
    """

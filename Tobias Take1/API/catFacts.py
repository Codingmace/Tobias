import requests

def catFact(maxLength):
    url = "https://catfact.ninja/facts"
    if maxLength >= 20:
        url += "?max_length=" + str(maxLength)    

    response = requests.request("GET", url)
    return response


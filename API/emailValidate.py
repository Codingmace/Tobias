import requests
from API.variables import rapidApiKey

def validEmail(email):
    url = "https://email-validator8.p.rapidapi.com/api/v2.0/email"
    payload = "email=" + email.replace("@","%40")

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "email-validator8.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

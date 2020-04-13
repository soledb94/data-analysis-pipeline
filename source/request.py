import requests 
import json 


def getFromOpenaq(city,measurement):

    if city=="Madrid":
        url = f"https://api.openaq.org/v1/latest?location=ES1938A&parameter={measurement}"
        res = requests.get(url)
        return res.json()
    elif city=="Barcelona":
        url = f"https://api.openaq.org/v1/latest?location=ES1396A&parameter={measurement}"
        res = requests.get(url)
        return res.json()



def getResult(request,city,measurement):
    request = getFromOpenaq(city,measurement)
    result=request["results"][0]["measurements"][0]["value"]
    return result
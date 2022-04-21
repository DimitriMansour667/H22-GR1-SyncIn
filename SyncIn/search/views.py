from django.shortcuts import render
import requests
import base64
import json
from secrets import *

# Create your views here.

def search (response): 
    return render(response, "search/index.html", {})

clientId = "5a3ae217ec7044f981b938869c691130"
clientSecret = "efaf289a8333490bb4e335ca85a83347"

def setUp():
    # Step 1 - Authorization 
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')


    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"

    r = requests.post(url, headers=headers, data=data)

    token = r.json()['access_token']
    
    return token


def getID(query): 
    token = setUp()
    
    length = 10

    searchUrl = f"https://api.spotify.com/v1/search?q=track:{query}&type=track&limit={length}"
    headers = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(url=searchUrl, headers=headers)

    resd = json.dumps(res.json(), indent=2)

    #print(resd)
    A = []
    for i in range(min(length, len(res.json()["tracks"]["items"]))):
        A.append(res.json()["tracks"]["items"][i]["id"])
    return A

def getName(id):
    token = setUp()
    
    length = 10

    searchUrl = f"https://api.spotify.com/v1/tracks/{id}"
    headers = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(url=searchUrl, headers=headers)

    resd = json.dumps(res.json(), indent=2)
    
    print(resd)
    return res.json()["name"]



def results (response, query): 
    print(query)

    list = getID(query)

    obj = {"title": getName(list[0]), "artist": "Aurora", "slug": list[0]}
    obj2 = {"title": getName(list[1]), "artist": "Kanye West", "slug": list[1]}
    return render(response, "results/index.html", {"results": [
        obj, obj2
    ]})
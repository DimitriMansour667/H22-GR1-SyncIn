from django.shortcuts import render
import requests
import base64
import json
#from SpotifySearch import *

# Create your views here.

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


def getID(id, token): 
    
    length = 10

    searchUrl = f"https://api.spotify.com/v1/tracks/{id}"
    headers = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(url=searchUrl, headers=headers)

    resd = json.dumps(res.json(), indent=2)

    
    
    parsed = res.json()

    featArray = []
    for i in range (len(parsed["artists"]) - 1): 
        featArray.append({"name": parsed["artists"][i + 1]["name"]})
        
    o = {
        "artist": {
            "main": {
                "name": parsed["artists"][0]["name"],
                "other": featArray
            }
        },
        "infos": {
            "title": parsed["name"],
            "duration": parsed["duration_ms"],
            "spotify": parsed["external_urls"]["spotify"],
        },
        "album": getImage(parsed["album"]["id"], token),
        "slug": parsed["id"],
    }
    return o

def getImage(albumID, token):
    
    searchUrl = f"https://api.spotify.com/v1/albums/{albumID}"
    headers = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(url=searchUrl, headers=headers)

    resd = json.dumps(res.json(), indent=2)

    print(resd.split("\"artists\": [")[1])

    parsed = res.json()

    o = {
        "image": parsed["images"][0]["url"],
        "name" : parsed["name"],
        "release-date": parsed["release_date"],
        "spotify": parsed["external_urls"] ["spotify"]
    }

    return o



def musics (response, music_slug): 
    token = setUp()

    objs = getID(music_slug, token)

    return render(response, "musics/index.html", {"results": objs})
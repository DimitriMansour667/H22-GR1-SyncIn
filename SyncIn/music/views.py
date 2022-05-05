from django.shortcuts import render
import requests
import base64
import json
import urllib.request
import wikipediaapi
import wikipedia
import math
import re
import lyricsgenius
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

    print(resd)
    
    parsed = res.json()

    featArray = []
    for i in range (len(parsed["artists"]) - 1): 
        featArray.append(getArtist(parsed["artists"][i + 1]["id"], token))

    duration = parsed["duration_ms"] / 1000
    durationO = {
        "minutes": math.floor(duration / 60),
        "seconds": math.floor(duration - math.floor(duration / 60) * 60)
    }
        
    o = {
        "artist": {
            "main": getArtist(parsed["artists"][0]["id"], token),
            "other": featArray
        },
        "infos": {
            "title": parsed["name"],
            "duration": durationO,
            "spotify": parsed["external_urls"]["spotify"],
            "youtube": getYoutube(parsed["name"] + parsed["artists"][0]["name"]),
            "lyrics": getLyrics(parsed["name"].split("(")[0], parsed["artists"][0]["name"])
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

    #print(resd.split("\"artists\": [")[1])

    parsed = res.json()

    o = {
        "image": parsed["images"][0]["url"],
        "name" : parsed["name"],
        "release-date": parsed["release_date"],
        "spotify": parsed["external_urls"] ["spotify"]
    }

def getArtist(ID, token):
    
    searchUrl = f"https://api.spotify.com/v1/artists/{ID}"
    headers = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(url=searchUrl, headers=headers)

    resd = json.dumps(res.json(), indent=2)

    #print(resd)

    parsed = res.json()
    #print (parsed["images"][1]["url"])

    o = {
        "name": parsed["name"], 
        "image": parsed["images"][1]["url"],
        "description": getDesc(parsed["name"])
    }

    return o

def getLyrics(songName, artist):
    key = "Y-RRX84gWlRVqXEc6K_yUQJdzs3gftwzVIPX0LXRFVY4QSprakvrTYUcOR-FvE_kuHSAeJeRwpX1VQsjiw9qBA"

    genius = lyricsgenius.Genius(key)

    song = genius.search_song(songName, artist)
    #print(songName, artist)
    #print(song.lyrics)
    return song.lyrics



    # # Encode as Base64
    # message = f"{clientId}:{clientSecret}"
    # messageBytes = message.encode('ascii')
    # base64Bytes = base64.b64encode(messageBytes)
    # base64Message = base64Bytes.decode('ascii')


    # headers['Authorization'] = f"Basic {base64Message}"
    # data['grant_type'] = "client_credentials"

    # r = requests.post(url, headers=headers, data=data)

    # token = r.json()['access_token']
    
    # return token

def getDesc(name):
    wiki_wiki = wikipediaapi.Wikipedia('fr')
    name = name.lower().title()

    formattedNames = ["_".join(name.split(" ")), name + "_(chanteur)", name + "_(chanteuse)"]

    for i in range (len(formattedNames)):
        page_py=wiki_wiki.page(formattedNames[i])
        if "musi" in page_py.summary[0:10000] or "DJ" in page_py.summary[0:10000] or "rap" in page_py.summary[0:10000] or "chant" in page_py.summary[0:10000]:
            return {"content": page_py.summary[0:300], "url": "https://fr.wikipedia.org/wiki/" + formattedNames[i], "found": True}
    
    return {"content": "Page Wikipédia inexistante", "url": "", "found": False}

    
    #print("https://fr.wikipedia.org/wiki/" + "_".join(name.split(" ")))

    

def getYoutube(name): 
    searchWordCleaned = name.replace(' ', '+')

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+searchWordCleaned)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]


# def getID(query, token): 
    
#     length = 10

#     searchUrl = f"https://api.spotify.com/v1/tracks/{id}"
#     headers = {
#         "Authorization": "Bearer " + token
#     }

#     res = requests.get(url=searchUrl, headers=headers)

#     resd = json.dumps(res.json(), indent=2)

#     #print(resd)
#     A = []
#     for i in range(min(length, len(res.json()["tracks"]["items"]))):
#         parsed = res.json()
#         A.append({
#             "title": parsed["name"],
#             "artist": parsed["artists"][0]["name"],
#             "cover_url": getImage(["album"]["id"], token),
#             "slug": parsed["tracks"]["items"][i]["id"],
#         })
#     return A


def musics (response, music_slug): 
    token = setUp()

    objs = getID(music_slug, token)

    return render(response, "musics/index.html", {"results": objs})
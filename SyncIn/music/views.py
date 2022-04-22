from django.shortcuts import render
from music.SpotifySearch import *

# Create your views here.

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


def getID(query, token): 
    
    length = 10

    searchUrl = f"https://api.spotify.com/v1/tracks/{id}"
    headers = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(url=searchUrl, headers=headers)

    resd = json.dumps(res.json(), indent=2)

    #print(resd)
    A = []
    for i in range(min(length, len(res.json()["tracks"]["items"]))):
        parsed = res.json()
        A.append({
            "title": parsed["name"],
            "artist": parsed["artists"][0]["name"],
            "cover_url": getImage(["album"]["id"], token),
            "slug": parsed["tracks"]["items"][i]["id"],
        })
    return A


def musics (response, music_slug): 
    o = {"name": music_slug}

    return render(response, "musics/index.html", o)
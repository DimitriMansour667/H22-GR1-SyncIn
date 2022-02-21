import requests
import base64
import json
from secrets import *

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

length = 10

searchQuery = "biere emile bilodeau"
searchUrl = f"https://api.spotify.com/v1/search?q=track:{searchQuery}&type=track&limit={length}"
headers = {
    "Authorization": "Bearer " + token
}

res = requests.get(url=searchUrl, headers=headers)

resd = json.dumps(res.json(), indent=2)

print(resd)
for i in range(min(length, len(res.json()["tracks"]["items"]))):
    print(res.json()["tracks"]["items"][i]["external_urls"]["spotify"])


import urllib.request

ArtistName = "Kanye West"
ArtistName = ArtistName.replace(' ', '_')
html = urllib.request.urlopen("https://en.wikipedia.org/wiki/" + ArtistName)

print(html.read().decode())
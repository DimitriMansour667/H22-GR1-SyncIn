import urllib.request
#permet de demander des urls
import re
#capable de trouver l'identifiant d'une video


searchWordBrute = input()
searchWordCleaned = searchWordBrute.replace(' ', '+')
searchResult = int(0)

html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+searchWordCleaned)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
for x in range(10) :
    print("https://www.youtube.com/watch?v=" + video_ids[searchResult])
    searchResult += 1

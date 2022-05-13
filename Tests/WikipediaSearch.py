import urllib.request
import wikipediaapi
import wikipedia

artist= input("Quel artiste souhaites tu chercher ")
#print(wikipedia.summary(artist))
print(wikipedia.page(artist).content)


wiki_wiki = wikipediaapi.Wikipedia('fr')
page_py=wiki_wiki.page('Kanye_West')

print("Page - Title: %s" % page_py.title)
 

print("Page - Summary: %s" % page_py.summary[0:10000].split("\n")[0])
   



#ArtistName = "Kanye West"
#ArtistName = ArtistName.replace(' ', '_')
#html = urllib.request.urlopen("https://en.wikipedia.org/wiki/" + ArtistName)

#print(html.read().decode())
from django.shortcuts import render
#from SpotifySearch import *

# Create your views here.




def musics (response, music_slug): 
    o = {"name": music_slug}

    return render(response, "musics/index.html", o)
from django.shortcuts import render

# Create your views here.

def search (response): 
    return render(response, "search/index.html", {})

obj = {"title": "Runaway", "artist": "Kanye West"}

def results (response): 
    return render(response, "results/index.html", {"results": [
        obj
    ], "foo": "bar"})
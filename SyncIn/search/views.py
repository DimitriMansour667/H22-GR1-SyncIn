from django.shortcuts import render

# Create your views here.

def search (response): 
    return render(response, "search/index.html", {})
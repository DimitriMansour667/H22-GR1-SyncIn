from django.shortcuts import render

# Create your views here.

def search (response): 
    return render(response, "search/index.html", {})

def results (response): 
    return render(response, "results/index.html", {})
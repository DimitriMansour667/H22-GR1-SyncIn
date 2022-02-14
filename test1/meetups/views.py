from django.shortcuts import render

# Create your views here.

def index(request):
    meetups = [
        {"title": "A first meetup", "location": "New York", "slug": "a-first-meetup"},
        {"title": "A second meetup", "location": "Paris", "slug": "a-second-meetup"}
    ]
    return render(request, "meetups/index.html", {
        "show_meetups": True,
        "meetups": meetups
    })
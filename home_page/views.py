from django.shortcuts import render

# Create your views here.
#homepage.py views

def home(request):
    return render(request, "homepage/home.html", {})
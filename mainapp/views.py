from django.shortcuts import render
import requests
import json
from .helper import helpr
# from .form import cityForm
# Create your views here.


def index(request):
    flag = 0
    if request.method == 'POST':
        city = request.POST["city"]
        weather_data = helpr(city)
    else:
        weather_data = helpr("London")
    if weather_data == -1:
        flag = 1
        weather_data = helpr("London")
        weather_data['error'] = 1

    context = {
        "weather_data": weather_data,
    }
    return render(request, "index.html", context)

import requests
import json


def helpr(city):
    api_key = "<api key>"
    url = "http://api.weatherapi.com/v1/forecast.json"

    data = {
        "key": api_key,
        "q": city,
        "days": 3,
    }

    res = requests.get(url, params=data).json()

    if "error" in res:
        return -1

    forecast = res["forecast"]["forecastday"]
    weather_data = {}

    # # # 1. Date
    # # # 2. Average Temp(C)
    # # # 3. Condition

    for i in range(len(forecast)):
        l = ['one', 'two', 'three']
        a = l[i]
        weather_data[a] = {"date": forecast[i]["date"],
                           "avg_temp": forecast[i]["day"]["avgtemp_c"],
                           "text": forecast[i]["day"]["condition"]["text"],
                           "icon": forecast[i]["day"]["condition"]["icon"],
                           "location": res["location"]["region"] + "/" + res["location"]["name"]
                           }
    return weather_data

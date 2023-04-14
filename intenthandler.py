# This file is where all the intent fulfillment is handled.
# It's essentially the part of code that does what the user wants, everything else is
# communication
import json
import random
import socket
import requests
import python_weather
import asyncio


def greeting(params: dict):
    possible_responses = ["Hello, how can I help you?", "Hi! What do you need?", "Hey, how can I be of assistance?",
                          "Hello! What's up?"]
    chosen_response = possible_responses[random.randint(0, 3)]
    return chosen_response


def weather(params: dict):
    if params['city'] == '':
        ip_address = socket.gethostbyname(socket.gethostname())
        print(ip_address)
        request_url = 'https://geolocation-db.com/jsonp/'
        response = requests.get(request_url)
        city = response.content.decode()
        city = city.split("(")[1].strip(")")
        cityName = json.loads(city)['city']
        if cityName == "Richmond" and json.loads(city)['state'] == "Texas":
            city = "Houston"
        else:
            city = cityName
    else:
        city = params['city']
    print("City: " + city)
    if params['weather_info'] == '':
        info = 'temperature'
    else:
        info = params['weather_info']
    print("info: "+info)
    return asyncio.run(get_weather(city, info))


async def get_weather(city, info):
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather_info = await client.get(city)

        if info == "temperature":
            return "It is " + str(weather_info.current.temperature) + " degrees Fahrenheit in " + city
        elif info == "feels like":
            return "It feels like " + str(weather_info.current.feels_like) + " in " + city
        elif info == "humidity":
            return "The humidity in " + city + " is " + str(weather_info.current.humidity) + "percent."
        else:
            return "uhhhhhhhh"

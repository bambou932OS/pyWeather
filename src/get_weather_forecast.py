import json
from urllib import request, error
from . import api_key_parser
import datetime
import pprint

def build_url_onecall(lat, lon, metric):
    # https://openweathermap.org/api/one-call-api
    try: 
        api_key = api_key_parser.get_api_key()
        if(len(api_key) == 0):
            raise Exception
        
    except: # api_key.ini 파일이 없거나, api_key.ini 파일이 올바른 형식이 아닐 때
        api_key_parser.make_api_key_file()

    metric_string = "metric" if metric else "imperial"

    return f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units={metric_string}"


def get_today_weather_forecast(weather_data):
    weather_list = []

    for weather in weather_data['hourly']:
        weather_list.append([weather['weather'][0]['description'], weather['temp'], weather['dt']]) # add weather discription, temperature, time(Unix time)

    weather_list.sort(key=lambda x: x[2]) # sort by time(Unix time)

    # Get today's weather forecast
    today_weather_forecast = []
    for weather in weather_list:
        if(datetime.datetime.fromtimestamp(weather[2]).date() == datetime.date.today()):
            today_weather_forecast.append(weather)

    # Get today's weather discreption by majority vote
    today_weather_discreption = []
    for weather in today_weather_forecast:
        today_weather_discreption.append(weather[0])

    today_weather_discreption = max(set(today_weather_discreption), key=today_weather_discreption.count) # Get the most frequent element in the list

    # Get today's weather temperature by average
    today_weather_temperature = 0
    for weather in today_weather_forecast:
        today_weather_temperature += weather[1]

    today_weather_temperature /= len(today_weather_forecast)

    return today_weather_discreption, today_weather_temperature


def get_onecall3_weather(weather_data, metric):
    # https://openweathermap.org/api/one-call-api
    # https://openweathermap.org/api/one-call-api#history
    # https://openweathermap.org/api/one-call-api#parameter
    
    query_url = build_url_onecall(weather_data['coord']['lat'], weather_data['coord']['lon'], metric)

    try:
        with request.urlopen(query_url) as response: # Get the response from the URL
            data = json.loads(response.read())

    except error.HTTPError as e: # If an HTTPError occurs (e.g., 404 Not Found)
        if(e.code == 400):
            print('400 Bad Request.')
            print('If this error occurs periodically, please report an issue')

        if(e.code == 401):
            print('Invalid API Key. Enter Valid API Key.')
            api_key_parser.make_api_key_file()

        if(e.code == 404):
            print('City not found. Please enter valid city name.')
            raise SystemExit

        if(e.code == 429):
            print('Too many requests. Please try again later.')
            raise SystemExit

        if(e.code//100 == 5): # 5xx Server Error
            print('Unexpected Error. Check Internet connection and try again later.')
            raise SystemExit
    
    #pprint.pprint(data)
    print(get_today_weather_forecast(data))
    return data
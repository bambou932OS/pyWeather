import json
from urllib import request, error
from . import api_key_parser # This is a relative import

def build_url_onecall(lat, lon, metric):
    # https://openweathermap.org/api/one-call-api
    try: 
        api_key = api_key_parser.get_api_key()
        if(len(api_key) == 0):
            raise Exception
        
    except: # api_key.ini 파일이 없거나, api_key.ini 파일이 올바른 형식이 아닐 때
        api_key_parser.make_api_key_file()

    return f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units={metric}"

def get_onecall3_weather(weather_data, metric, api_key):
    # https://openweathermap.org/api/one-call-api
    # https://openweathermap.org/api/one-call-api#history
    # https://openweathermap.org/api/one-call-api#parameter

    query_url = build_url_onecall(weather_data['lat'], weather_data['lon'], metric, api_key_parser.get_api_key())

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
        
    return data
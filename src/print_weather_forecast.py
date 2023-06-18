# Print weather information
import pprint
import datetime

def print_weather_forecast(weather_data, metric=True):
    #pprint.pprint(weather_data)
    weather_dt = datetime.datetime.fromtimestamp(weather_data['dt'])
    print(
        f'Weather on {weather_dt.strftime("%m/%d")} in {weather_data["name"]}({weather_data["country"]}) '
        f'is {weather_data["temp"]}°{"C" if metric else "F"}, {weather_data["description"].capitalize()}'
    )

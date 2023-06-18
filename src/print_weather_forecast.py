# Print weather information
import pprint
import datetime

def print_weather_forecast(weather_data, metric=True):
    #pprint.pprint(weather_data)
    weather_dt = datetime.datetime.fromtimestamp(weather_data['dt'])
    print(
        f'Weather in {weather_data["name"]}({weather_data["country"]}) on {weather_dt.strftime("%m/%d")} '
        f'is {weather_data["temp"]:.2f}°{"C" if metric else "F"}, {weather_data["description"].capitalize()}'
    )

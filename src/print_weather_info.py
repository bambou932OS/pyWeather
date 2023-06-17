# Print weather information
import pprint

# 출력할때 색깔을 입히기 위한 함수
def colorize(text:str, background_color_code:str, text_color_code:str, length:int=0) -> str:
    if(length == 0): length = len(text) # length가 주어지지 않았으면, text의 길이로 설정

    text_color = f'\u001b[38;5;256{text_color_code}m'
    background_color = f'\u001b[48;5;256{background_color_code}m'
    
    return f'{background_color}{text_color}{text:^{length}}\u001b[0m'

def print_weather_info(weather_data, metric=True):
    #pprint.pprint(weather_data)
    print(
        colorize(weather_data["name"]+f'({weather_data["sys"]["country"]})', 7, 0, 15) +
        f'    {weather_data["main"]["temp"]}°{"C" if metric else "F"}, {weather_data["weather"][0]["description"].capitalize()}'
    )

# Print weather information
import pprint

# Make dictionary for weather id and color code
weather_id_color_code = {
    200: 11, 201: 11, 202: 11, 210: 11, 211: 11, 212: 11, 221: 11, 230: 11, 231: 11, 232: 11, # Yellow(11) for Thunderstorm
    300: 20, 301: 20, 302: 20, 310: 20, 311: 20, 312: 20, 313: 20, 314: 20, 321: 20, # Blue3(20) for Drizzle
    500: 18, 501: 18, 502: 18, 503: 18, 504: 18, 511: 18, 520: 18, 521: 18, 522: 18, 531: 18, # DarkBlue(18) for Rain
    600: 255, 601: 255, 602: 255, 611: 255, 612: 255, 613: 255, 615: 255, 616: 255, 620: 255, 621: 255, 622: 255, # Grey93(255) for Snow
    
    701: 241, # Grey39(241) for Mist
    711: 215, # SandyBrown(215) for Smoke
    721: 241, # Grey39(241) for Haze
    731: 215, # SandyBrown(215) for Dust
    741: 241, # Grey39(241) for Fog
    751: 215, # SandyBrown(215) for Sand
    761: 215, # SandyBrown(215) for Dust
    762: 208, # DarkOrange(208) for Ash
    771: 57, # BlueViolet(57) for Squall
    781: 196, # Red1(196) for Tornado

    800: 87, #DarkSlateGray2(87) for Clear sky
    801: 7, 802: 7, 803: 7, 804: 7 # Silver(7) for Clouds
}

# 출력할때 색깔을 입히기 위한 함수
def colorize(text:str, background_color_code:str, text_color_code:str, length:int=0) -> str:
    if(length == 0): length = len(text) # length가 주어지지 않았으면, text의 길이로 설정

    text_color = f'\u001b[38;5;256{text_color_code}m'
    background_color = f'\u001b[48;5;256{background_color_code}m'
    
    return f'{background_color}{text_color}{text:^{length}}\u001b[0m'

def print_weather_info(weather_data, metric=True):
    #pprint.pprint(weather_data)
    print(
        # City part
        colorize(f'({weather_data["sys"]["country"]})', "7", "0") +
        colorize(weather_data["name"], "7", "0", 17-len(weather_data["sys"]["country"])) +
        colorize(' '*(len(weather_data["sys"]["country"]) + 2), "7", "0") +

        # Weather part
        f' ' * 8 + 
        f'{weather_data["main"]["temp"]:.02f}°{"C" if metric else "F"}' +
        f' ' * 8 +

        colorize(f'{weather_data["weather"][0]["description"].capitalize():^15}', weather_id_color_code[weather_data["weather"][0]["id"]], "0")
    )

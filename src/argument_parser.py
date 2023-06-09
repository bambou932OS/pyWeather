import sys
import argparse

def parse_method(parse_str :str):
    return parse_str.split()

def get_args(): # Get the command-line arguments
    parser = argparse.ArgumentParser(description='Get the weather forecast for a given location.')

    parser.add_argument('location', metavar='location', type= parse_method, nargs='+', help='The location to get the weather forecast.')
    # Celsius scale, 섭씨 온도 척도
    parser.add_argument('-c', '-m', '--metric', dest='metric', action='store_true', help='Use metric units instead of imperial.')
    # Fahrenheit scale, 화씨 온도 척도
    parser.add_argument('-f', '-i', '--imperial', dest='metric', action='store_false', help='Use imperial units instead of metric.')
    # Weather forecast, 날씨 예보
    parser.add_argument('-fc', '--forecast', dest='forecast', action='store_true', help='Get the weather forecast for today.')

    parser.set_defaults(metric=True)
    parser.set_defaults(weather=True)
    parser.set_defaults(forecast=False)

    return parser.parse_args() # Return the parsed arguments
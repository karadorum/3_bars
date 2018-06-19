import json
import requests
from math import sqrt


def load_data(filepath):
    with open(filepath, encoding="utf-8") as json_file:
        parsed_string = json.load(json_file)
        return parsed_string


def get_biggest_bar(bars_data):
    bars = bars_data['features']
    biggest_bar = max(bars, key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar["properties"]["Attributes"]['Name']


def get_smallest_bar(bars_data):
    bars = bars_data['features']
    smallest_bar = min(bars, key=lambda k: k["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar["properties"]["Attributes"]['Name']


def get_distance(bar, longitude, latitude):
    bar_longitude, bar_latitude = bar["geometry"]["coordinates"]
    distance = sqrt((bar_latitude - latitude)**2 + (bar_longitude - longitude)**2)
    return distance


def get_closest_bar(bars_data, longitude, latitude):
    closest_bar = min(
        bars_data['features'],
        key=lambda x: get_distance(x, longitude, latitude)
    )
    return(closest_bar["properties"]["Attributes"]['Name'])


if __name__ == '__main__':
    filepath = input('Введите путь к файлу: ')
    bars_data = load_data(filepath)

    print('Самый большой бар: ', get_biggest_bar(bars_data))
    print('Самый маленький бар: ', get_smallest_bar(bars_data))
    print('Самый близкий бар: ',  get_closest_bar(
        bars_data, longitude=float(input('Your longitude: ')),
        latitude=float(input('Your latitude: '))))
        
import json
from math import sqrt
import os
import sys


def load_data(filename):
    with open(filename, encoding='utf-8') as json_file:
        decoded_json = json.load(json_file)
        return decoded_json


def get_biggest_bar(bars_data):
    biggest_bar = max(
        bars_data,
        key=lambda k: k['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars_data):
    smallest_bar = min(
        bars_data,
        key=lambda k: k['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_distance(bar, longitude, latitude):
    bar_longitude, bar_latitude = bar['geometry']['coordinates']
    distance = sqrt((bar_latitude - latitude)**2 + (bar_longitude - longitude)**2)
    return distance


def get_closest_bar(bars_data, longitude, latitude):
    closest_bar = min(
        bars_data,
        key=lambda x: get_distance(x, longitude, latitude)
    )
    return closest_bar


def get_arg(argname):
    try:
        x = float(input('Your {}: '.format(argname)))
    except ValueError:
        x = None
        print('{} must be number'.format(argname))
    return x


def get_bars(arg):
    try:
        arg_data = load_data(arg)['features']
    except IndexError:
        exit('name of file argument is empty')
    except FileNotFoundError:
        exit('file not found')
    except json.decoder.JSONDecodeError:
        exit('file format must be json')
    return arg_data


def print_result(bar_description, bar):
    bar_name = bar['properties']['Attributes']['Name']
    print(bar_description, bar_name)


if __name__ == '__main__':
    longitude = get_arg('longitude')
    latitude = get_arg('latitude')
    bars_data = get_bars(sys.argv[1])

    print_result(
        'Самый большой бар: ',
        get_biggest_bar(bars_data))
    print_result(
        'Самый маленький бар: ',
        get_smallest_bar(bars_data))
    print_result(
        'Самый близкий бар: ',
        get_closest_bar(
            bars_data,
            longitude,
            latitude
            ))

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
        return x
    except ValueError:
        print('{} must be number'.format(argname))


def print_bar(bar_description, bar):
    bar_name = bar['properties']['Attributes']['Name']
    print(bar_description, bar_name)


if __name__ == '__main__':
    try:
        bars_data = load_data(sys.argv[1])['features']
    except IndexError:
        print('name of file argument is empty')
    except FileNotFoundError:
        print('file not found')
    except json.decoder.JSONDecodeError:
        print('file must be json')

    longitude = get_arg('longitude')
    latitude = get_arg('latitude')

    print_bar(
        'Самый большой бар: ',
        get_biggest_bar(bars_data))
    print_bar(
        'Самый маленький бар: ',
        get_smallest_bar(bars_data))
    print_bar(
        'Самый близкий бар: ',
        get_closest_bar(
            bars_data,
            longitude,
            latitude
            ))

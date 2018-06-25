import json
import requests
from math import sqrt
import os
import sys


def load_data(filename):
    with open(filename, encoding='utf-8') as json_file:
        json_decoded = json.load(json_file)
        return json_decoded


def get_biggest_bar(bars_data):
    max_bar_capacity = max(bars_data['features'], key=lambda k: k['properties']['Attributes']['SeatsCount'])
    biggest_bar = max_bar_capacity['properties']['Attributes']['Name']
    return biggest_bar


def get_smallest_bar(bars_data):
    min_bar_capacity = min(bars_data['features'], key=lambda k: k['properties']['Attributes']['SeatsCount'])
    smallest_bar = min_bar_capacity['properties']['Attributes']['Name']
    return smallest_bar


def get_distance(bar, longitude, latitude):
    bar_longitude, bar_latitude = bar['geometry']['coordinates']
    distance = sqrt((bar_latitude - latitude)**2 + (bar_longitude - longitude)**2)
    return distance


def get_closest_bar(bars_data, longitude, latitude):
    min_bar_distance = min(
        bars_data['features'],
        key=lambda x: get_distance(x, longitude, latitude)
    )
    closest_bar = min_bar_distance['properties']['Attributes']['Name']
    return closest_bar


if __name__ == '__main__':
    try:
        longitude = float(input('Your longitude: '))
    except ValueError:
        longitude = None
        print('longitude,latitude must be numbers')
    try:
        latitude = float(input('Your latitude: '))
    except ValueError:
        latitude = None
        print('longitude,latitude must be numbers')

    bars_data = load_data(sys.argv[1])

    print('Самый большой бар: ', get_biggest_bar(bars_data))
    print('Самый маленький бар: ', get_smallest_bar(bars_data))
    print('Самый близкий бар: ',  get_closest_bar(
        bars_data, longitude, latitude))

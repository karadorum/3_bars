import json
import requests
from math import sqrt
filepath = 'https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json'


def load_data(filepath):
    response = requests.get(filepath)
    # получаем файл по ссылке
    parsed_string = json.loads(response.text)
    # преобразуем в обычный текст
    return parsed_string


json_data = load_data(filepath)
# сохраняем функцию в перменную


def get_biggest_bar(json_data):
    bars_seats = {}
    # создаем пустой словарь
    for bar in range(len(json_data["features"])):
        bars_seats.update({
            json_data["features"][bar]["properties"]["Attributes"]["Name"]:
            json_data["features"][bar]["properties"]["Attributes"]["SeatsCount"]
        })  # наполняем словарь парами {Название : Кол-во мест}
        key_max = max(bars_seats.keys(), key=(lambda k: bars_seats[k]))
        # находим максимальное значение кол-ва мест
    print('Biggest bar: ' + key_max)
    # выводим на экран ключ от максимального значения


def get_smallest_bar(json_data):
    bars_seats = {}
    for bar in range(len(json_data)+1):
        bars_seats.update({
            json_data["features"][bar]["properties"]["Attributes"]["Name"]:
            json_data["features"][bar]["properties"]["Attributes"]["SeatsCount"]
        })
        key_min = min(bars_seats.keys(), key=(lambda k: bars_seats[k]))
    print('Smallest bar: ' + key_min)


def get_closest_bar(json_data, lon, lat):

    bars_way = {}
    # создаем пустой словарь
    for bar in range(len(json_data["features"])):
        # читаем файл
        lat_of_bar = json_data["features"][bar]["geometry"]["coordinates"][0]
        # широта, записываем в переменную для удобства
        lon_of_bar = json_data["features"][bar]["geometry"]["coordinates"][1]
        # долгота, записываем в переменную для удобства
        dist = sqrt((lat_of_bar - lat)**2 + (lon_of_bar - lon)**2)
        # представляем что земля плоская и считаем расстояние
        # между нами и каждым баром по теореме Пифагора
        bars_way.update({
            json_data["features"][bar]["properties"]["Attributes"]["Name"]:
            # в пустой словарь добавляем пары {название : расстояние}
            dist
        })

        key_min = min(bars_way.keys(), key=(lambda k: bars_way[k]))
        # находим минимальное значение расстояния
    print('Nearest bar: ' + key_min)
    # выводим на экран ключ от минимального значения


if __name__ == '__main__':
    get_biggest_bar(json_data)
    get_smallest_bar(json_data)
    get_closest_bar(
        json_data, lon=float(input('Your longitude: ')),
        lat=float(input('Your latitude: ')))
# просим пользователя ввести свои координаты

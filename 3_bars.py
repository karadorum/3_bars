import json
import requests
from math import sqrt
filepath = 'https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json'


def load_data(filepath):
    r = requests.get(filepath)
    # получаем файл по ссылке
    parsed_string = json.loads(r.text)
    # преобразуем в обычный текст
    return parsed_string


data = load_data(filepath)
# сохраняем функцию в перменную


def get_biggest_bar(data):
    d = {}
    # создаем пустой словарь
    for i in range(0, len(data["features"])):
        d.update({
            data["features"][i]["properties"]["Attributes"]["Name"]:
            data["features"][i]["properties"]["Attributes"]["SeatsCount"]
        })  # наполняем словарь парами {Название : Кол-во мест}
        key_max = max(d.keys(), key=(lambda k: d[k]))
        # находим максимальное значение кол-ва мест
    print('Biggest bar: ' + key_max)
    # выводим на экран ключ от максимального значения


def get_smallest_bar(data):
    d = {}
    for i in range(0, len(data)+1):
        d.update({
            data["features"][i]["properties"]["Attributes"]["Name"]:
            data["features"][i]["properties"]["Attributes"]["SeatsCount"]
        })
        key_min = min(d.keys(), key=(lambda k: d[k]))
    print('Smallest bar: ' + key_min)


def get_closest_bar(data, lon, lat):

    r = {}
    # создаем пустой словарь
    for i in range(0, len(data["features"])):
        # читаем файл
        c = data["features"][i]["geometry"]["coordinates"][0]
        # широта, записываем в переменную для удобства
        d = data["features"][i]["geometry"]["coordinates"][1]
        # долгота, записываем в переменную для удобства
        dist = sqrt((c - lon)**2 + (d - lat)**2)
        # представляем что земля плоская и считаем расстояние
        # между нами и каждым баром по теореме Пифагора
        r.update({
            data["features"][i]["properties"]["Attributes"]["Name"]:
            # в пустой словарь добавляем пары {название : расстояние}
            dist
        })

        key_min = min(r.keys(), key=(lambda k: r[k]))
        # находим минимальное значение расстояния
    print('Nearest bar: ' + key_min)
    # выводим на экран ключ от минимального значения


if __name__ == '__main__':
    get_biggest_bar(data)
    get_smallest_bar(data)
    get_closest_bar(
        data, lon=float(input('Your longitude: ')),
        lat=float(input('Your latitude: ')))
# просим пользователя ввести свои координаты

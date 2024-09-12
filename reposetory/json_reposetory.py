import json
from functools import partial
from toolz import pluck, pipe, get_in, first, compose
from models.weather import Weather
from models.locations import Location
from typing import List
from operator import itemgetter


def convert_json_to_weather(json):

    main_getter = compose(itemgetter('main'),first,itemgetter('weather'))
    wind_getter = partial(get_in, ['wind', 'speed'])
    date_getter = itemgetter('dt_txt')
    cloud_getter = partial(get_in, ['clouds', 'all'])

    return pipe(
        json,
        itemgetter("list"),
        partial(map, lambda e: Weather(
            main=main_getter(e),
            wind=wind_getter(e),
            date=date_getter(e),
            clouds=cloud_getter(e)
        )),
        list
    )


class WeatherEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Weather):
            return obj.__dict__
        return super().default(obj)


class LocationEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Location):
            return obj.__dict__
        return super().default(obj)


def write_weathers_to_json(weathers: List[Weather], filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(weathers, jsonfile, cls=WeatherEncoder, indent=4)


def read_weathers_from_json(filename: str) -> List[Weather]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Weather(weather['main'], weather['clouds'], weather['wind'], weather['date']) for weather in data]


def write_weather_to_json(weather: Weather, filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(weather.__dict__, jsonfile, indent=4)


def read_weather_from_json(filename: str) -> Weather:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return Weather(data['main'], data['clouds'], data['wind'], data['date'])


def write_locations_to_json(locations: List[Location], filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(locations, jsonfile, cls=LocationEncoder, indent=4)


def read_locations_from_json(filename: str) -> List[Location]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Location(location['lat'], location['lon']) for location in data]


def write_location_to_json(location: Location, filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(location.__dict__, jsonfile, indent=4)


def read_location_from_json(filename: str) -> Weather:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return Location(data['lat'], data['lon'])


def read_target_name(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return pipe(
            data,
            partial(pluck, "Target City"),
            list
        )

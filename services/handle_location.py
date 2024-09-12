from api.weather_api import get_weather, get_location
from reposetory.json_reposetory import read_target_name, write_locations_to_json, convert_json_to_weather
from toolz import pipe, partial, pluck, keyfilter
from operator import itemgetter
from functools import reduce


def get_all_locations():
    target_names = read_target_name("../reposetory/targets.json")
    locations = []
    for name in target_names:
        api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={name}&appid=0923f4fcd7a0f5907d2adcf9736a5999"
        locations.append(get_location(api_url))
    return locations


print(get_all_locations())


def write_to_json(locations):
    write_locations_to_json(locations, "../reposetory/locations.json")


print(write_to_json(get_all_locations()))

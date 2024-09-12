from api.weather_api import get_weather
from reposetory.json_reposetory import read_target_name, write_weathers_to_json, convert_json_to_weather
from toolz import pipe, partial, pluck, keyfilter
from operator import itemgetter
from functools import reduce


def get_all_wethers():
    target_names = read_target_name("../reposetory/targets.json")
    weathers = []
    for name in target_names:
        api_url = f"https://api.openweathermap.org/data/2.5/forecast?q={name}&appid=0923f4fcd7a0f5907d2adcf9736a5999"

        weathers.append(convert_json_to_weather(get_weather(api_url)))
    return weathers


def filter_weathers_by_time(weathers):
    return pipe(
        weathers,
        #partial(filter, lambda u: 'list' in u),
        #partial(pluck, "list"),
        #partial(reduce, lambda a, n: a + n),

        partial(filter, lambda u: '00:00:00' in u['dt_txt']),
        list
    )


def write_to_json(weathers):
    write_weathers_to_json(weathers, "../reposetory/filterd_weathers.json")


write_to_json(get_all_wethers())
def weather_score(weather):
    if weather['condition'] == "Clear":
        return 1.0
    elif weather['condition'] == "Clouds":
        return 0.7
    elif weather['condition'] == "Rain":
        return 0.4
    elif weather['condition'] == "Stormy":
        return 0.2
    else:
        return 0

import requests


def get_weather(url):
    response = requests.request("GET", url)
    return response.json()


def get_location(url):
    try:
        response = requests.request("GET", url)
        return response.json()
    except Exception as e:
        print(f"Error {e}")
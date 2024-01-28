import requests
import json

from datetime import datetime
from typing import NamedTuple,Literal
from enum import Enum
from math import ceil

from fake_useragent import UserAgent

from gps_coordinates import Coordinates,GetHTTPResponse
from gps_coordinates import DeserializeJsonHTTPResponse
from exceptions import CantGetWeatherWithAPI

query = {
    'User-Agent': UserAgent().random
}

class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    CLOUDS = "Облачно"

Kelvins = int

class Weather(NamedTuple):
    tempreture: Kelvins
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime

def get_current_weather(coordinates: Coordinates) -> Weather:
    """Gives you current weather"""
    try:
        data = _GetData(coordinates)
        weather = _ParseWeather(data)
    except Exception:
        raise CantGetWeatherWithAPI
    
    return weather

def _format_url(coordinates: Coordinates):
    
    latitude = coordinates.latitude
    longitude = coordinates.longitude

    return f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&lang=ru&appid=0f3f0cec744ca8001c1a873db0ff7449'

def _ParseTempreture(data):
    
    return int((float(data['main']['temp']) - 273.15))

def _ParseWeatherType(data):

    return data['weather'][0]['description']

def _parse_suntime(data, time: Literal['sunrise'] | Literal['sunset']):
    return datetime.fromtimestamp(data['sys'][time])
def _ParseWeather(data):

    tempreture = _ParseTempreture(data)
    weather_type = _ParseWeatherType(data)
    sunrise = _parse_suntime(data,'sunrise')
    sunset = _parse_suntime(data,'sunset')

    weather = _FormWeather(tempreture,weather_type,sunrise,sunset)

    return weather

def _FormWeather(tempreture,weather_type,sunrise,sunset):

    return Weather(
        tempreture=tempreture,
        weather_type=weather_type,
        sunrise=sunrise,
        sunset=sunset
    )

def _GetData(coordinates):
    url = _format_url(coordinates)
    response = GetHTTPResponse(url, query)
    
    return DeserializeJsonHTTPResponse(response.text)
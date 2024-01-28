from weather_api_service import Weather

def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (f"температура {weather.tempreture}°C ",
            f"{weather.weather_type}",
            f"Восход: {weather.sunrise.strftime('%H:%M')}",
            f"Закат: {weather.sunset.strftime('%H:%M')}")


from pathlib import Path

from gps_coordinates import Coordinates, get_coordinates
from weather_api_service import get_current_weather
from weather_formatter import format_weather 

from HistoryStrorage import save_weather, JsonFileWeatherStorage



def main() -> None:
    """Giving you current weather"""
    OwnCoordinates: Coordinates = get_coordinates()
    weather = get_current_weather(OwnCoordinates)
    formatedWeather = format_weather(weather)
    for part in formatedWeather:
        print(part) 

    save_weather(
        weather,
        JsonFileWeatherStorage(Path.cwd() / "history.json")
    )

if __name__=="__main__":
    main()
from datetime import datetime 
import json
from typing import TypedDict
from pathlib import Path

from weather_api_service import Weather
from weather_formatter import format_weather


class WeatherStorage:
    """Interface for any storage saving weather"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError
    
class HistoryRecord(TypedDict):
    date: str
    weather: str

class JsonFileWeatherStorage(WeatherStorage):
    """Store weather in plain text file"""
    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        FormatedWeather = format_weather(weather)
        with open(self._file, "a") as f:
            f.write(f"{now}\n{[part for part in FormatedWeather]}")
            f.write('\n')
    def _init_storage(self) ->None:
        if not self._jsonfile.exists():
            self._jsonfile.write_text("[]")
    def _read_history(self) -> list[HistoryRecord]:
        with open(self._jsonfile, "r") as f:
            return json.load(f)
    def _write(self, history: list[HistoryRecord]) ->None:
        with open(self._jsonfile, "w") as f:
            json.dump(history,f,ensure_ascii=False, indent=4)

def save_weather(weather: Weather, storage: WeatherStorage):
    """Saves wheather in storage"""
    storage.save(weather)
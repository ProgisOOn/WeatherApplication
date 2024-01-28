import json
import requests

from exceptions import CantGetCoordinates
from fake_useragent import UserAgent
from typing import NamedTuple

from pprint import pprint


class Coordinates(NamedTuple):
    latitude:float
    longitude: float

def get_coordinates() -> Coordinates:
    try:
        lattitude, longitude = GetLattitudeAndLongitude()
    except Exception:
        raise CantGetCoordinates
    

    return Coordinates(latitude=lattitude,longitude=longitude)

def GetHTTPResponse(url,query):
    """Send http request with headers"""

    return requests.get(url, headers=query)

def DeserializeJsonHTTPResponse(HTTPBody: json):
    """Makes from HTTP json python object: Dict """

    return json.loads(HTTPBody)

def ParseMyLocation (data: dict[str,str]):   
    """Parse location from gotten json"""
    return data['loc']

def ParseCoordinates(Location: str):
    """Parse lattitude and longitude from string"""
    return Location.strip().split(',')

def GetLattitudeAndLongitude():

    query = {
    'User-Agent' : UserAgent().random
}
    response = GetHTTPResponse(url='https://ipinfo.io/json',query=query)
    data = DeserializeJsonHTTPResponse(response.text)
    FullLocation = ParseMyLocation(data)

    return ParseCoordinates(FullLocation)
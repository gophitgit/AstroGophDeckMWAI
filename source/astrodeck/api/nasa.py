# source\astrodeck\api\nasa.py
import requests

from astrodeck.config import NASA_API_KEY


BASE_URL = "https://api.nasa.gov"


def check_asteroids(start_date, end_date) -> dict:
    url = f"{BASE_URL}/neo/rest/v1/feed"

    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": NASA_API_KEY,
    }

    response = requests.get(
        url,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()

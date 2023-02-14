import os
import requests

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
tequila_endpoint = "https://api.tequila.kiwi.com"
headers = {
    "apikey": TEQUILA_API_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city_name):
        query_config = {
            "term": city_name,
            "location_types": "city",
            "limit": 1
        }
        response = requests.get(url=f"{tequila_endpoint}/locations/query", params=query_config, headers=headers)
        code = response.json()["locations"][0]["code"]
        return code


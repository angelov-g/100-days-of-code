import os
import requests
import datetime as dt
from flight_data import FlightData

tomorrow_date = dt.datetime.today() + dt.timedelta(days=1)
six_months_date = tomorrow_date + dt.timedelta(days=180)

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

    def find_flight(self, destination_code):
        search_config = {
            "fly_from": "LON",
            "fly_to": f"{destination_code}",
            "date_from": tomorrow_date.strftime("%d/%m/%Y"),
            "date_to": six_months_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0,
        }
        response = requests.get(url=f"{tequila_endpoint}/v2/search", params=search_config, headers=headers)
        result = response.json()['data'][0]
        flight_data = FlightData(
            price=result['price'],
            origin_city=result['cityFrom'],
            origin_airport=result['flyFrom'],
            destination_city=result['cityTo'],
            destination_airport=result['flyTo'],
            out_date=result['route'][0]['local_departure'].split("T")[0],
            return_date=result['route'][1]['local_departure'].split("T")[0],
        )
        # print(f"{flight_data.destination_city[0]} : £{flight_data.price}")
        return flight_data

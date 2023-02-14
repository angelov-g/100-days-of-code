import os
import requests

SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")
sheety_endpoint = f"https://api.sheety.co/{SHEETY_API_KEY}/flightClub/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def get_sheet_data(self):
        response = requests.get(url=sheety_endpoint)
        sheet_data = response.json()["prices"]
        return sheet_data

    def update_sheet_data(self, sheet_data):
        for entry in sheet_data:
            entry_config = {
                "price": {
                    "city": entry["city"],
                    "iataCode": entry["iataCode"],
                    "lowestPrice": entry["lowestPrice"]
                }
            }
            requests.put(url=f"{sheety_endpoint}/{entry['id']}", json=entry_config)

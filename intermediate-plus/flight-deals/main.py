# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from prices import prices
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Will not work because of insufficient requests
# sheet_data = data_manager.get_sheet_data()

# Import sample dictionary from local file.
sheet_data = prices
# pprint(sheet_data)

# Check for empty IATA Code fields and fill them
for entry in sheet_data:
    if entry["iataCode"] == "":
        entry["iataCode"] = flight_search.get_iata_code(entry["city"])

# Will not work because of insufficient requests
# data_manager.update_sheet_data(sheet_data)

for entry in sheet_data:
    flight_data = flight_search.find_flight(entry["iataCode"])

    if flight_data is None:
        continue
    else:
        if flight_data.price < entry["lowestPrice"]:
            print(notification_manager.send_notification(flight_data))

# pprint(sheet_data)

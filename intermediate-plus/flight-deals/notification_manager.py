# NotificationManager should use the TWILIO SMS API, but I will use just a simple print to console.

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, flight_data):
        message = f"Low price alert! Only £{flight_data.price} to fly from\n" \
                  f"{flight_data.origin_city}-{flight_data.origin_airport[0]} to " \
                  f"{flight_data.destination_city[0]}-{flight_data.destination_airport[0]},\n" \
                  f"from {flight_data.out_date[0]} to {flight_data.return_date}."
        return message

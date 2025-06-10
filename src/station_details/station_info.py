import requests
from dotenv import load_dotenv
import os

class StationInfo:

    def get_station_info(self):
        station_name = input("Enter station name: ")
        result = self.station_info(station=station_name)
        if result:
            print(result)
        else:
            print("No station information found.")

    def station_info(self, station):
        load_dotenv()
        API_KEY = os.getenv("API_KEY")

        if not API_KEY:
            print("Error: API_KEY not found in environment variables.")
            return None

        url = f"https://indianrailapi.com/api/v2/AutoCompleteStation/apikey/{API_KEY}/StationCodeOrName/{station}/"
        try:
            response = requests.get(url)
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)

            if response.status_code == 200:
                try:
                    info = response.json()
                    return info.get("Station", None)
                except ValueError as ve:
                    print("JSON decode error:", ve)
                    return None
            else:
                print("Failed request:", response.status_code)
                return None

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None

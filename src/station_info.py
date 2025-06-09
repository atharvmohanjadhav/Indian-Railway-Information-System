import requests
from dotenv import load_dotenv
import os

class StationInfo:

    def get_station_info(self):
        station_name = input("Enter station name:")
        self.station_info(station=station_name)

    load_dotenv()
    def station_info(self,station):
        API_KEY = os.getenv("API_KEY")
        info = requests.get(f"https://indianrailapi.com/api/v2/AutoCompleteStation/apikey/{API_KEY}/StationCodeOrName/{station}/")
        info = info.json()
        print(info["Station"])

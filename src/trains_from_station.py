import requests 
import os
from dotenv import load_dotenv

class TrainFromStation:
    def __init__(self) -> None:
        pass

    def get_trains_from_station(self):
        station_code = input("Enter station code:")
        self.trains_info(station_code=station_code)
        
    load_dotenv()
    def trains_info(self,station_code):
        API_KEY = os.getenv("API_KEY")
        info = requests.get(f"http://indianrailapi.com/api/v2/AllTrainOnStation/apikey/{API_KEY}/StationCode/{station_code}/")

        info = info.json()
        print(info['Trains'])
    
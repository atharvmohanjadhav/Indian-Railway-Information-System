import requests 
import os
from dotenv import load_dotenv
from utils.custom_exception import IrisException
import sys

class TrainFromStation:
 
    def get_trains_from_station(self):
        station_code = input("Enter station code:")
        result = self.trains_info(station_code=station_code)
        if result:
            print(result)
        else:
            print("info not found")
        
    load_dotenv()
    def trains_info(self,station_code):
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            print("Api key not found")
            return
        url = f"https://indianrailapi.com/api/v2/AllTrainOnStation/apikey/{API_KEY}/StationCode/{station_code}/"
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                try:
                    info = response.json()
                    return info.get("Trains",None)
                except Exception as e:
                    raise IrisException(e,sys)
            else:
                print("Failed request:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print(e)

    
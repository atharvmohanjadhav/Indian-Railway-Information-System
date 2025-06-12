from dotenv import load_dotenv
from utils.custom_exception import IrisException
import os
import sys
import requests

class StationToCode:
    def __init__(self) -> None:
        pass

    load_dotenv()
    def station_to_code_info(self,station_name):
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            print("Invalid API KEY")
            return
        url = f"https://indianrailapi.com/api/v2/StationNameToCode/apikey/{API_KEY}/StationName/{station_name}/"
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                try:
                    info = response.json()
                    station_data = info.get("Station",None)
                    if station_data:
                        return station_data.get("StationCode", None)
                    else:
                        print("Station info not found!")
                except IrisException as e:
                    raise (e,sys)
            else:
                print("reques failed",response.status_code)
        except requests.exceptions.RequestException as e:
            print(e)
        
    

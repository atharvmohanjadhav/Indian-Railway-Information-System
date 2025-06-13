import requests 
import os
from dotenv import load_dotenv
from utils.custom_exception import IrisException
import sys

class PremiumTrains:
    def __init__(self) -> None:
        pass

    load_dotenv()
    def premium_trains_info(self):
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            print("Api key not found")
            return
        url = f"https://indianrailapi.com/api/v2/PremiumTrains/apikey/{API_KEY}/"
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                try:
                    info = response.json()
                    return info.get("Trains",None)
                except IrisException as e:
                    raise (e,sys)
            else:
                print("Failed request:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print(e)

    
import requests 
import os
from dotenv import load_dotenv
from utils.custom_exception import IrisException
import sys

class RajdhaniTrains:
    def __init__(self) -> None:
        pass

    load_dotenv()
    def rajdhani_trains_info(self):
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            print("Api key not found")
            return
        url = f"https://indianrailapi.com/api/v2/RajdhaniTrain/apikey/{API_KEY}/"
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

    
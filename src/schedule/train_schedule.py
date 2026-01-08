import requests
import os
from dotenv import load_dotenv
import sys
from utils.custom_exception import IrisException

class TrainSchedule:

    def __init__(self):
        pass

    def train_schedule_info(self):
        train_no = int(input("Enter train number:"))
        result = self.get_info(train_number=train_no)
        if result:
            print(result)
        else:
            print("No info found")

    load_dotenv()
    def get_info(self,train_number:int) -> str:
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            print("API key not found!")
            return
        
        url = f"https://indianrailapi.com/api/v2/TrainSchedule/apikey/{API_KEY}/TrainNumber/{train_number}/"
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                try:
                    info = response.json()
                    return info.get("Route",None)
                except Exception as e:
                    raise IrisException(e,sys)
            else:
                print("Failed request:", response.status_code)
                return None
            
        except requests.exceptions.RequestException as e:
            print(e)
            return

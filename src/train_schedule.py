import requests
import os
from dotenv import load_dotenv

class TrainSchedule:

    def __init__(self):
        pass

    def train_schedule_info(self):
        train_no = int(input("Enter train number:"))
        self.get_info(train_number=train_no)

    load_dotenv()
    def get_info(self,train_number):
        API_KEY = os.getenv("API_KEY")
        info = requests.get(f"https://indianrailapi.com/api/v2/TrainSchedule/apikey/{API_KEY}/TrainNumber/{train_number}/")
        info = info.json()
        for i in info["Route"]:
            print("|" + i["StationName"] + "|" + i["ArrivalTime"] + "|" + i["DepartureTime"] + "|")
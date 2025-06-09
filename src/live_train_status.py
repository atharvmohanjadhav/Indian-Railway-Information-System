import requests 
import os
from dotenv import load_dotenv

class LiveTrainStatus:
    def __init__(self) -> None:
        pass

    def get_live_status(self):
        train_no = input("Enter train number:")
        date = input("Enter date (yyyymmdd):")
        self.get_info(train_number=train_no,date=date)
        
    load_dotenv()
    def get_info(self,train_number,date):
        API_KEY = os.getenv("API_KEY")
        info = requests.get(f"http://indianrailapi.com/api/v2/livetrainstatus/apikey/{API_KEY}/trainnumber/{train_number}/date/{date}/")

        info = info.json()
        print(info['Message'])
    
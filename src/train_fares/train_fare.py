from dotenv import load_dotenv
import os
import requests
from utils.custom_exception import IrisException
import sys
class TrainFare:

    def get_train_fare(self):
        train_no = input("Enter train number:")
        src_station = input("Enter source station: ")
        dest_station = input("Enter destination station")
        quota = input("Enter quata (e.g GN,CK): ")
        self.train_fare_datail(train_no=train_no,src_station=src_station,dest_station=dest_station,quata=quota)
        
    load_dotenv()
    def train_fare_datail(self,train_no,src_station,dest_station,quata):
        API_KEY = os.getenv("API_KEY")

        if not API_KEY:
            print("Invalid API KEY")
            return
        
        url = f"https://indianrailapi.com/api/v2/TrainFare/apikey/{API_KEY}/TrainNumber/{train_no}/From/{src_station}/To/{dest_station}/Quota/{quata}"
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                try:
                    info = response.json()
                    return info.get("Fares",None)
                except IrisException as e:
                    raise (e,sys)
            else:
                print("Request Failed",response.status_code)
                return None
                
        except requests.exceptions.RequestException as e:
            print(e)
            return


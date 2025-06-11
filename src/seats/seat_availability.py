from utils.custom_exception import IrisException
from dotenv import load_dotenv
import requests
import os
import sys

class SeatAvailability:

    def get_seat_availability(self):
        train_no = input("Enter train number:")
        src_station = input("Enter source station: ")
        dest_station = input("Enter destination station")
        reservation_date = input("Enter date:")
        class_code = input("Enter quata (e.g GN,CK): ")
        self.get_seat_availability_info(train_no=train_no,src_station=src_station,dest_station=dest_station,reservation_date=reservation_date,class_code=class_code)

    load_dotenv()
    def get_seat_availability_info(self,train_no,src_station,dest_station,reservation_date,class_code):
        API_KEY = os.getenv("API_KEY")

        if not API_KEY:
            print("API KEY not found")
            return 
        
        url = f"https://indianrailapi.com/api/v2/SeatAvailability/apikey/{API_KEY}/TrainNumber/{train_no}/From/{src_station}/To/{dest_station}/Date/{reservation_date}/Quota/GN/Class/{class_code}"
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                try:
                    info = response.json()
                    return info.get("Availability",None)
                except IrisException as e:
                    raise (e,sys)
            else:
                print("Resuqest Failed",response.status_code)
                return
            
        except requests.exceptions.RequestException as e:
            print(e)




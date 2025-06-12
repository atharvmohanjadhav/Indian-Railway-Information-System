from dotenv import load_dotenv
from utils.custom_exception import IrisException
import os
import sys
import requests

class TrainNoToName:
    def __init__(self) -> None:
        pass

    load_dotenv()
    def train_no_to_name_info(self,train_no):
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            print("Invalid API KEY")
            return
        url = f"http://indianrailapi.com/api/v2/TrainNumberToName/apikey/{API_KEY}/TrainNumber/{train_no}/"
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                try:
                    info = response.json()
                    return info.get("TrainName",None)
                    
                except IrisException as e:
                    raise (e,sys)
            else:
                print("reques failed",response.status_code)
        except requests.exceptions.RequestException as e:
            print(e)
        
    

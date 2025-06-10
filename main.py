from dotenv import load_dotenv
from src.schedule.train_schedule import TrainSchedule
from src.live_train_status import LiveTrainStatus
from src.station_details.station_info import StationInfo
from src.trains_from_station import TrainFromStation

class IRCTC:
    def __init__(self):
        user_ip = input("""
        1. Enter 1 to check live location of train.
        2. Enter 2 to check station info.
        3. Enter 3 to check train status. 
        4. Enter 4 to all trains from station        
            """)
        
        if user_ip == "1":
            LiveTrainStatus().get_live_status()
        elif user_ip == "2":
            StationInfo().get_station_info()
        elif user_ip == "3":
            TrainSchedule().train_schedule_info()
        elif user_ip == "4":
            TrainFromStation().get_trains_from_station()
        else:
            exit


obj = IRCTC()

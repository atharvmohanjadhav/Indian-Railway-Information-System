from dotenv import load_dotenv
from src.train_schedule import TrainSchedule
from src.live_train_status import LiveTrainStatus

class IRCTC:
    def __init__(self):
        user_ip = input("""
        1. Enter 1 to check live location of train.
        2. Enter 2 to check PNR.
        3. Enter 3 to check train status.         
            """)
        
        if user_ip == "1":
            LiveTrainStatus().get_live_status()
        elif user_ip == "2":
            pass
        else:
            TrainSchedule().train_schedule_info()

obj = IRCTC()

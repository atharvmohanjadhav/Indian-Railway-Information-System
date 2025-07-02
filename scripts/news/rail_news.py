import requests
from dotenv import load_dotenv
import os
from utils.custom_exception import IrisException
import sys

load_dotenv()

def fetch_railway_news():
    try:
        api_key = os.getenv("NEWS_API_KEY")
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q=Indian%20Railways&"
            f"sortBy=publishedAt&"
            f"language=en&"
            f"apiKey={api_key}"
        )

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["articles"][:10] 
        else:
            return []
    except Exception as e:
        raise IrisException(e,sys)
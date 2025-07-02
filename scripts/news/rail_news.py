import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_railway_news():
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
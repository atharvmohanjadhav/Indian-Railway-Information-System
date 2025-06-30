from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from utils.custom_exception import IrisException
import os
import sys

class ExtractStationInfo:
    def __init__(self, api_key):
        self.api_key = api_key

    def extract_station_info(self):
        try:
            model = ChatGroq(
                model="llama-3.3-70b-versatile",
                api_key=self.api_key
            )

            parser = StrOutputParser()

            return model | parser

        except Exception as e:
            raise IrisException(e, sys)

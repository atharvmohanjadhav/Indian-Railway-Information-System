from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.custom_exception import IrisException
import os
import sys


class SearchTrain:
    def __init__(self,api_key):
        self.api_key = api_key
    
    def search(self):
        try:
            prompt = PromptTemplate(
                template= """
                    You are a smart railway assistant. Based on the following details:
                    - Source: {source}
                    - Destination: {destination}
                    - Date: {date}
                    - Time: {time}

                    suggest me a list of available trains on that day. If time is provided, use it as a filter.
                    """,
                        input_variables=["source", "destination", "date", "time"]
            )
            model = ChatGroq(
                model="llama-3.3-70b-versatile",
                api_key=self.api_key
            )

            parser = StrOutputParser()

            chain = prompt | model | parser

            return chain
        except Exception as e:
            raise IrisException(e,sys)
    
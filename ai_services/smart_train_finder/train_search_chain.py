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
                        template="""
                    You are a smart Railway Assistant.

                    Based on the following travel details:
                    - Source: {source}
                    - Destination: {destination}
                    - Date: {date}
                    - Time: {time}

                    Your tasks:
                    1. Find and suggest a list of **available direct trains** for this route on the specified date (and time, if provided).

                    2. If there are **no direct trains**, or the direct options are very limited, then:
                    - Identify **possible connecting routes** via major junctions or intermediate stations.
                    - Suggest logical **via routes** (e.g., Source ➝ Junction ➝ Destination) that are practical and minimize total travel time.
                    - Include train names/numbers for each leg, if possible.

                    3. Present the information in a clear, structured format that is easy for the user to read.

                    Be clear and helpful. If real-time data is missing, politely remind the user to check the official railway site or app for final confirmation.
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
    
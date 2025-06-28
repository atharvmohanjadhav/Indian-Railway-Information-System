from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from utils.custom_exception import IrisException
import os
import sys

class Extract:
    def __init__(self,api_key):
        self.api_key = api_key

    def extract_features(self):
        try:
            prompt = PromptTemplate(
                template= """You are a railway assistant. Extract the following fields from user query: 
                - source (station name)
                - destination (station name)
                - date (of travel)
                - time (optional)
            Query: {query}
            Return output ONLY in this JSON format:
            {{"source":"", "destination":"", "date":"", "time":""}}
            """,
                input_variables=["query"]
            )

            model = ChatGroq(
                model="llama-3.3-70b-versatile",
                api_key=self.api_key
            )

            parser = JsonOutputParser()

            chain = prompt | model | parser

            return chain
        except Exception as e:
            raise IrisException(e,sys)




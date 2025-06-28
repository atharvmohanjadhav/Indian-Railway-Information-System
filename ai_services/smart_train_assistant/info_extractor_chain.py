from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from utils.custom_exception import IrisException
import os
import sys

class ExtractInfo:
    def __init__(self, api_key):
        self.api_key = api_key

    def extract_info(self):
        """
        Return a Runnable that accepts full message history.
        """
        try:
            # ✅ Load your Groq model
            model = ChatGroq(
                model="llama-3.3-70b-versatile",
                api_key=self.api_key
            )

            # ✅ Use a simple StrOutputParser (optional)
            parser = StrOutputParser()

            # ✅ For full chat flow, you don’t need PromptTemplate:
            # Just pass the entire chat history
            return model | parser

        except Exception as e:
            raise IrisException(e, sys)

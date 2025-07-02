from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from utils.custom_exception import IrisException
from utils.prompt_templates import train_finder_prompt
import sys

class Extract:
    def __init__(self,api_key):
        self.api_key = api_key

    def extract_features(self):
        try:
            prompt = PromptTemplate(
                template= train_finder_prompt,
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




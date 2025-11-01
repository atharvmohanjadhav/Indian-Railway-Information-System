from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
# from langchain.schema.runnable import RunnableBranch,RunnableLambda
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import Field,BaseModel
from typing import Literal
from utils.custom_exception import IrisException
import sys


from dotenv import load_dotenv
load_dotenv()

class Feedback(BaseModel):
    sentiment: Literal["positive","negative"] = Field(description="Give the sentiment of the feedback")
try:
    def get_feedback(text):

        model = ChatGroq(model="llama-3.3-70b-versatile")

        parser = StrOutputParser()
        parser2 = PydanticOutputParser(pydantic_object=Feedback)

        prompt1 = PromptTemplate(
            template= "classify the sentiment of the following feedback text into 1 word e.g positive or negative. \n {feedback} \n {format_instruction}",
            input_variables=['feedback'],
            partial_variables={'format_instruction':parser2.get_format_instructions()}
        )

        classsifier_chain = prompt1 | model | parser2

        pos_prompt = PromptTemplate(
            template="write an 3 lines apropriate resposnse to this positive feedback. \n {feedback}",
            input_variables=['feedback']
        )

        neg_prompt = PromptTemplate(
            template="write an 3 lines apropriate resposnse to this negative feedback. \n {feedback}",
            input_variables=['feedback']
        )

        branch_chain = RunnableBranch(
            (lambda x: x.sentiment == "positive", pos_prompt | model | parser),
            (lambda x: x.sentiment == "negative", neg_prompt | model | parser),
            RunnableLambda(lambda x : "could not find sentiment") 
        )

        final_chain = classsifier_chain | branch_chain
        res = final_chain.invoke(text)
        return res

except Exception as e:
    raise IrisException(e,sys)
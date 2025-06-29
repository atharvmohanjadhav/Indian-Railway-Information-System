from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

from langchain_core.prompts import PromptTemplate

train_chatbot_prompt = PromptTemplate(
    template="""
        You are a intelliegent langauge translator. only translate give text into hindi language

        text: {text}
        """,
    input_variables=["text"]
)


parser = StrOutputParser()

chain = train_chatbot_prompt | model | parser

res = chain.invoke({"text":"i love india"})
print(res)

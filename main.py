from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

prompt1 = PromptTemplate(
    template="""
        You are a helpful assistant with expert knowledge of Indian Railway stations.

        The user will ask questions about any Indian railway station. Your task is to:
        - Understand which station is being asked about
        - Identify the intent (e.g., facilities, platforms, retiring rooms, cleanliness, etc.)
        - Respond accurately and concisely with relevant information

        User Query: {query}

        Answer:
        """,
    input_variables=["query"]
)

# prompt2 = PromptTemplate(
#     template="explain the following joke {text}",
#     input_variables=['text']
# )

parser = StrOutputParser()

chain = prompt1 | model | parser

res = chain.invoke({"query":"give me a deatailed information about chiplun"})
print(res)
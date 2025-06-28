from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

# from langchain_core.prompts import PromptTemplate

# train_chatbot_prompt = PromptTemplate(
#     template="""
# You are a knowledgeable and friendly Railway AI Assistant.

# Your role is to answer **any** question the user asks about a specific Indian train.
# This includes but is not limited to:  
# - Schedule & timings  
# - Route & important stops  
# - Fares & ticket classes  
# - Punctuality & average delay  
# - Facilities (pantry, Wi-Fi, seating)  
# - Coach composition  
# - History and background  
# - Any other detail the user wants to know.

# Use clear, conversational language.
# If you don't have enough information, politely mention that the user should verify with the official railway website or inquiry counter.

# Always make your answer detailed but easy to read.

# **User Query:**  
# {query}

# **Answer:**
# """,
#     input_variables=["query"]
# )



# # prompt2 = PromptTemplate(
# #     template="explain the following joke {text}",
# #     input_variables=['text']
# # )

# parser = StrOutputParser()

# chain = train_chatbot_prompt | model | parser

# res = chain.invoke({"query":"tell me about history train konkan kanya express"})
# print(res)

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# load_dotenv()

#model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)
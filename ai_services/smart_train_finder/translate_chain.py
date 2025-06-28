from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

translation_prompt = PromptTemplate(
    template="""
        You are a translator. Please translate the following text into {language}:
        ---
        {text}
        """,
    input_variables=["text", "language"]
)

def get_translation_chain(api_key):
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=api_key
    )
    parser = StrOutputParser()
    return translation_prompt | model | parser

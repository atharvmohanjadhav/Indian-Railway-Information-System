from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from utils.prompt_templates import language_translate_prompt

translation_prompt = PromptTemplate(
    template=language_translate_prompt,
    input_variables=["text", "language"]
)

def get_translation_chain(api_key):
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=api_key
    )
    parser = StrOutputParser()
    return translation_prompt | model | parser

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.prompt_templates import story_teller_prompt
class GenerateStory:
    def __init__(self,api_key) -> None:
        self.api_key = api_key

    def generate_story(self,mood,genre,duration):
        prompt = PromptTemplate(
            template=story_teller_prompt,
            input_variables=['mood','genre',"duration"]
        )

        llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=self.api_key)

        parser = StrOutputParser()

        chain = prompt | llm | parser

        res = chain.invoke({"mood":mood,"genre":genre,"duration":duration})
        return res
    
        









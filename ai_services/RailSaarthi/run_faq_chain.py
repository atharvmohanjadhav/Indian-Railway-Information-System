from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq 
from ai_services.RailSaarthi.ingest import vector_store
from utils.custom_exception import IrisException
import sys

class FaqChain:

    def __init__(self,api_key) -> None:
        self.api_key = api_key

    def get_data(self):
        try:

            # 1️⃣ Load your saved index
            # vectorstore = FAISS.load_local(
            #     "railsaarthi_faq_index",
            #     embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
            # )

            # 2️⃣ Build the prompt
            faq_prompt = PromptTemplate(
                template="""
            You are RailSaarthi, a helpful Indian Railways FAQ assistant.
            Answer the user question using ONLY the context below.
            If the context doesn't contain enough information, say politely you don't have answer tell reffer to official website.

            Context:
            {context}

            User Question:
            {question}

            Answer:
            """,
                input_variables=["context", "question"]
            )

            # 3️⃣ Setup Retrieval QA chain
            llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=self.api_key)
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=vector_store.as_retriever(search_type="similarity",search_kwargs={"k": 5}),
                chain_type_kwargs={"prompt": faq_prompt}
            )

            return qa_chain
        except Exception as e:
            raise IrisException(e,sys)


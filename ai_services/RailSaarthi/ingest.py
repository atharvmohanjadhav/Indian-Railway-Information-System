from pinecone import Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from utils.load_json import load_faq_json
from utils.custom_exception import IrisException
import sys

load_dotenv()

try:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    pc = Pinecone(api_key=PINECONE_API_KEY)

    index_name = "indian-railway-system"  

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    index = pc.Index(index_name)

    embeddings = HuggingFaceEmbeddings()

    vector_store = PineconeVectorStore(index=index, embedding=embeddings)

    # print("data created succesfully")

    documents = load_faq_json(json_file="indian_railway_faqs.json")

    vector_store.add_documents(documents=documents)
except Exception as e:
    raise IrisException(e,sys)

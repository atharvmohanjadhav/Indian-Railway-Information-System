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

# try:
#     PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
#     pc = Pinecone(api_key=PINECONE_API_KEY)

#     index_name = "indian-railway-system"  

#     if not pc.has_index(index_name):
#         pc.create_index(
#             name=index_name,
#             dimension=768,
#             metric="cosine",
#             spec=ServerlessSpec(cloud="aws", region="us-east-1"),
#         )

#     index = pc.Index(index_name)

#     embeddings = HuggingFaceEmbeddings()

#     vector_store = PineconeVectorStore(index=index, embedding=embeddings)

#     documents = load_faq_json(json_file="indian_railway_faqs.json")

#     vector_store.add_documents(documents=documents)
# except Exception as e:
#     raise IrisException(e,sys)

# Move initialization inside a function to prevent run-on-import
def get_vector_store():
    try:
        load_dotenv()
        PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        
        if not PINECONE_API_KEY:
            raise ValueError("PINECONE_API_KEY not found in environment variables")

        pc = Pinecone(api_key=PINECONE_API_KEY)
        index_name = "indian-railway-system"
        
        # We assume index exists or create it safely
        # Note: In production, index creation should usually be a separate setup script
        if index_name not in pc.list_indexes().names():
             pc.create_index(
                name=index_name,
                dimension=768,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        index = pc.Index(index_name)
        embeddings = HuggingFaceEmbeddings()
        
        vector_store = PineconeVectorStore(index=index, embedding=embeddings)
        return vector_store

    except Exception as e:
        raise IrisException(e, sys)

# This block ensures data is ONLY uploaded when you run this file directly
# e.g., 'python ai_services/RailSaarthi/ingest.py'
if __name__ == "__main__":
    try:
        print("Starting ingestion...")
        vector_store = get_vector_store()
        documents = load_faq_json(json_file="indian_railway_faqs.json")
        vector_store.add_documents(documents=documents)
        print("Ingestion complete!")
    except Exception as e:
        print(f"Ingestion failed: {e}")
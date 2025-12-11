
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
import sys
# Import streamlit to access secrets on Cloud
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from utils.load_json import load_faq_json
from utils.custom_exception import IrisException

# Wrap logic in a function
def get_vector_store():
    try:
        load_dotenv()
        
        # 1. Fetch PINECONE_API_KEY (Check .env first, then Secrets)
        PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        if not PINECONE_API_KEY and hasattr(st, "secrets"):
            PINECONE_API_KEY = st.secrets.get("PINECONE_API_KEY")
            
        if not PINECONE_API_KEY: 
            raise ValueError("PINECONE_API_KEY not found. Check .env or Streamlit Secrets.")

        # 2. Fetch HF_TOKEN (Crucial for fixing 429 Errors)
        HF_TOKEN = os.getenv("HF_TOKEN")
        if not HF_TOKEN and hasattr(st, "secrets"):
            HF_TOKEN = st.secrets.get("HF_TOKEN")
        
        # Set it as an environment variable so huggingface_hub detects it automatically
        if HF_TOKEN:
            os.environ["HF_TOKEN"] = HF_TOKEN

        # 3. Initialize Pinecone
        pc = Pinecone(api_key=PINECONE_API_KEY)
        index_name = "indian-railway-system"

        # Check if index exists before creating
        existing_indexes = [i.name for i in pc.list_indexes()]
        if index_name not in existing_indexes:
            pc.create_index(
                name=index_name,
                dimension=768,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        index = pc.Index(index_name)
        
        # 4. Initialize Embeddings (Now authenticated via os.environ['HF_TOKEN'])
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        
        vector_store = PineconeVectorStore(index=index, embedding=embeddings)
        return vector_store

    except Exception as e:
        # Re-raise nicely formatted exception
        raise IrisException(e, sys)

# Only run this if executed directly (e.g., for local setup)
if __name__ == "__main__":
    try:
        print("Starting Ingestion...")
        vector_store = get_vector_store()
        
        # Load data only if running script manually
        print("Loading FAQs...")
        documents = load_faq_json(json_file="indian_railway_faqs.json")
        
        print(f"Adding {len(documents)} documents to Pinecone...")
        vector_store.add_documents(documents=documents)
        print("Ingestion Complete!")
        
    except Exception as e:
        print(f"Ingestion Failed: {e}")
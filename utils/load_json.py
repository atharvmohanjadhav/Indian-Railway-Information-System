import json
from langchain_core.documents import Document

def load_faq_json(json_file: str) -> list:
    docs = []

    with open(json_file, 'r', encoding='utf-8') as f:
        faqs = json.load(f)

    for faq in faqs:
        question = faq.get("question", "")
        answer = faq.get("answer", "")
        category = faq.get("category", "")

        content = f"Question: {question}\nAnswer: {answer}"

        docs.append(
            Document(
                page_content=content,
                metadata={
                    "category": category
                }
            )
        )

    return docs


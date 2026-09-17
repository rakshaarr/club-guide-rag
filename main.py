import numpy as np
import faiss

from sentence_transformers import SentenceTransformer
from google import genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config import API_KEY

client = genai.Client(api_key=API_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("club_info.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = text.split("\n")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: Question):

    question = data.question

    question_embedding = model.encode([question])
    question_embedding = np.array(question_embedding).astype("float32")

    distances, indices = index.search(question_embedding, 1)

    result = chunks[indices[0][0]]

    prompt = f"""
Answer the question using only the information provided below.

If the information does not contain the answer, say that the information
is not available in the campus knowledge base.

Understand the meaning of the question even if the exact words are different.

Information:
{result}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return {
        "answer": response.text
    }
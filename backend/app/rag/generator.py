from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(question, chunks):
    context = "\n\n".join(chunks)

    prompt = f"""
You are an expert software engineer analyzing a codebase.

Instructions:
- Explain clearly
- Mention file names when possible
- Reference functions/classes
- Keep answer structured

Code Context:
{context}

Question:
{question}

Answer:
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )

    return response.choices[0].message.content
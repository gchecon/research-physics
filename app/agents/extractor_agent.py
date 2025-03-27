from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_abstract(text):
    prompt = f"""
    A seguir está o texto de um artigo científico. Extraia o *abstract* ou resumo caso esteja presente.

    Texto:
    {text[:3000]}  # Corte de segurança para tokens
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
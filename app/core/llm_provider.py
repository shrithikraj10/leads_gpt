import google.generativeai as genai
from fastapi import HTTPException
from openai import OpenAI, RateLimitError
from app.core.config import settings

openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
genai.configure(api_key=settings.GOOGLE_API_KEY)

def generate_with_openai(prompt: str):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content
    except RateLimitError:
        raise RuntimeError("OpenAI quota exceeded")

def generate_with_gemini(prompt: str):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # or a free model like "text-bison-001"
        response = model.generate_content(
            contents=[{
                "parts": [{"text": prompt}]
            }]
        )
        return response.text
    except Exception as e:
        raise RuntimeError(f"Gemini failed: {e}")

def generate_with_fallback(prompt: str):
    try:
        return generate_with_openai(prompt)
    except Exception as e1:
        try:
            return generate_with_gemini(prompt)
        except Exception as e2:
            raise HTTPException(
                status_code=500,
                detail=f"All providers failed:\nOpenAI: {e1}\nGemini: {e2}"
            )

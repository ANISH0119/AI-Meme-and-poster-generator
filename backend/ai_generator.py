import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

def generate_caption(topic, tone):
    prompt = f"""
You are a creative copywriter.

Generate ONE short poster caption for a college event.

Event topic: {topic}
Tone: {tone}

Rules:
- Be creative and different every time
- Do NOT repeat generic phrases
- Do NOT use 'you shouldn't miss'
- Keep it under 20 words
- Sound natural and human

Only return the caption text.
"""

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.9,
                "max_output_tokens": 60
            }
        )

        if not response.text:
            raise ValueError("Empty AI response")

        return response.text.strip()

    except Exception as e:
    print("Gemini error:", e)
    return f"{topic}: Experience it differently."

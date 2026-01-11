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
    Generate a short, creative {tone} caption for a college event poster.
    Topic: {topic}
    Keep it natural, catchy, and student-friendly.
    """

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        return text[:180]
    except Exception:
        return f"{topic} – An event you should not miss."

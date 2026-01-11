import os
import random
import google.generativeai as genai

# -----------------------------
# Configure Gemini
# -----------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

# -----------------------------
# Caption generation logic
# -----------------------------

BANNED_PHRASES = [
    "you shouldn't miss",
    "you should not miss",
    "dont miss",
    "don't miss",
    "do not miss",
    "unmissable",
    "must attend",
    "must-attend",
    "highlight of the day"
]

FALLBACK_CAPTIONS = [
    "{topic}. Built for curious minds.",
    "Where {topic} meets fresh ideas.",
    "{topic}: Not your usual event.",
    "A new perspective on {topic}.",
    "{topic}. Think beyond the obvious.",
    "Experience {topic} differently.",
    "More than an event. It’s {topic}.",
    "{topic}. Created for thinkers."
]

def generate_caption(topic, tone):
    """
    Generates a short, non-generic AI caption for a poster.
    Tries Gemini multiple times and blocks generic phrases.
    """

    prompt = f"""
You are a creative human copywriter.

Generate ONE short poster caption for a college event.

Event topic: {topic}
Tone: {tone}

Rules:
- Be original and non-generic
- Do NOT use phrases like "don't miss" or "must attend"
- Max 15 words
- Sound natural and human
- No hashtags
- Return ONLY the caption text
"""

    # Try Gemini up to 3 times
    for _ in range(3):
        try:
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 1.0,
                    "max_output_tokens": 50
                }
            )

            if not response or not response.text:
                continue

            caption = response.text.strip()

            # Normalize for checking
            lower_caption = caption.lower()

            # Reject generic captions
            if any(phrase in lower_caption for phrase in BANNED_PHRASES):
                continue

            # Reject very short / useless outputs
            if len(caption.split()) < 3:
                continue

            return caption

        except Exception as e:
            print("Gemini error:", e)

    # Final fallback (still non-generic)
    template = random.choice(FALLBACK_CAPTIONS)
    return template.format(topic=topic)

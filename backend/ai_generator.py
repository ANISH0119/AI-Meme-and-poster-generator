import os
import random
import google.generativeai as genai

# -----------------------------
# Gemini setup (used once only)
# -----------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# Hard rules
# -----------------------------

GENERIC_PHRASES = [
    "you shouldn't miss",
    "you should not miss",
    "don't miss",
    "do not miss",
    "unmissable",
    "must attend",
    "must-attend",
    "highlight of the day",
    "join us for",
    "exciting event"
]

# High-quality fallback pool (this is the key)
CAPTION_POOL = {
    "funny": [
        "Because seriousness is overrated.",
        "Laugh first. Regret later.",
        "Zero seriousness. Maximum chaos.",
        "Where logic takes a coffee break.",
        "Proof that fun is still legal."
    ],
    "formal": [
        "Ideas worth paying attention to.",
        "Where discussion meets direction.",
        "A space for informed thinking.",
        "Structured conversations that matter.",
        "Knowledge without the noise."
    ],
    "motivational": [
        "Start where ideas get uncomfortable.",
        "Build what others only imagine.",
        "This is where momentum begins.",
        "Push limits. Then redefine them.",
        "Designed for people who act."
    ]
}

def _is_generic(text: str) -> bool:
    text = text.lower()
    return any(p in text for p in GENERIC_PHRASES) or len(text.split()) < 4

# -----------------------------
# Main caption generator
# -----------------------------

def generate_caption(topic, tone):
    """
    GUARANTEED VARIATION STRATEGY:
    1. Try Gemini ONCE
    2. If generic -> discard
    3. Always return a strong caption from pool
    """

    prompt = f"""
Create ONE short poster caption.

Event: {topic}
Tone: {tone}

Rules:
- No marketing language
- No invitations
- No generic phrases
- Max 12 words
Return ONLY the caption.
"""

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 40
            }
        )

        if response and response.text:
            caption = response.text.strip()
            if not _is_generic(caption):
                return caption

    except Exception as e:
        print("Gemini error:", e)

    # FINAL GUARANTEED NON-GENERIC OUTPUT
    base = random.choice(CAPTION_POOL.get(tone, CAPTION_POOL["formal"]))
    return f"{topic}. {base}"

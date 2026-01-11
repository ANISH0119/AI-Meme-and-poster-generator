import os
import random

try:
    from openai import OpenAI, RateLimitError
    OPENAI_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=OPENAI_KEY) if OPENAI_KEY else None
except Exception:
    client = None
    RateLimitError = Exception


FALLBACK_CAPTIONS = {
    "funny": [
        "Because seriousness needed a break.",
        "Logic stepped out for a while.",
        "Fun approved. Sense optional.",
        "Where rules quietly disappear.",
        "Proof that fun still exists."
    ],
    "formal": [
        "A space for thoughtful discussion.",
        "Ideas presented with clarity.",
        "Structured thinking begins here.",
        "Where knowledge meets purpose.",
        "Conversations that matter."
    ],
    "motivational": [
        "Start where ideas take shape.",
        "Build what others hesitate to begin.",
        "Momentum begins with action.",
        "Push limits. Redefine outcomes.",
        "Designed for people who move forward."
    ]
}

def generate_caption(topic, tone):
    # Try OpenAI only if client exists
    if client:
        try:
            prompt = f"""
Create ONE short, creative poster caption.

Event: {topic}
Tone: {tone}

Rules:
- Max 12 words
- No marketing phrases
- No "don't miss"
- Natural language
Return ONLY the caption.
"""
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt,
                temperature=0.8,
                max_output_tokens=40
            )
            return response.output_text.strip()

        except RateLimitError:
            pass
        except Exception as e:
            print("OpenAI error:", e)

    # Fallback (always works)
    base = random.choice(FALLBACK_CAPTIONS.get(tone, FALLBACK_CAPTIONS["formal"]))
    return f"{topic}. {base}"

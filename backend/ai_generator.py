import random

CAPTIONS = {
    "funny": [
        "Because seriousness needed a break.",
        "Laughs included. Logic optional.",
        "Fun happened. Academics approved.",
        "Where rules quietly disappear.",
        "Proof that fun still exists."
    ],
    "formal": [
        "A space for thoughtful discussion.",
        "Ideas presented with purpose.",
        "Structured thinking starts here.",
        "Where knowledge meets clarity.",
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
    base = random.choice(CAPTIONS.get(tone, CAPTIONS["formal"]))
    return f"{topic}. {base}"

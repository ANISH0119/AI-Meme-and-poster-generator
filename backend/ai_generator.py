import random

CAPTIONS = {
    "funny": [
        "Because seriousness needed a break.",
        "Logic stepped out for a while.",
        "Fun approved. Sense optional.",
        "Where rules quietly disappear.",
        "Proof that fun still exists.",
        "Laughs were inevitable."
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
    base = random.choice(CAPTIONS.get(tone, CAPTIONS["formal"]))
    return f"{topic}. {base}"

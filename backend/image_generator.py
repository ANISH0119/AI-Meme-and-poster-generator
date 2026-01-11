from PIL import Image, ImageDraw, ImageFont
import io
import textwrap
import os
import time

FONT_MAP = {
    "funny": "fonts/ComicSansMS.ttf",
    "formal": "fonts/Arial.ttf",
    "motivational": "fonts/Impact.ttf"
}

OUTPUT_DIR = "outputs"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_poster(text, template_name, tone="formal"):
    # Load template
    img = Image.open(f"templates/{template_name}").convert("RGB")
    draw = ImageDraw.Draw(img)

    width, height = img.size

    # Dynamic font size based on poster width
    font_size = int(width * 0.06)

    # Select font based on tone
    font_path = FONT_MAP.get(tone, FONT_MAP["formal"])

    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception:
        font = ImageFont.load_default()

    # Dynamic wrapping
    chars_per_line = max(15, int(width / (font_size * 0.6)))
    wrapped_text = textwrap.fill(text, width=chars_per_line)

    # Measure text
    bbox = draw.multiline_textbbox(
        (0, 0),
        wrapped_text,
        font=font,
        align="center"
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Position text
    x = (width - text_width) / 2
    y = height * 0.30

    # Draw text
    draw.multiline_text(
        (x, y),
        wrapped_text,
        fill="black",
        font=font,
        align="center"
    )

    # Generate unique filename
    filename = f"poster_{int(time.time())}.png"
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Save to outputs folder
    img.save(output_path, format="PNG")

    # Also return image in memory for frontend
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer, output_path

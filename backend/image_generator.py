from PIL import Image, ImageDraw, ImageFont
import io
import textwrap

FONT_MAP = {
    "funny": "fonts/ComicSansMS.ttf",
    "formal": "fonts/Arial.ttf",
    "motivational": "fonts/Impact.ttf"
}

def create_poster(caption, template_name, tone):
    img = Image.open(f"templates/{template_name}").convert("RGB")
    draw = ImageDraw.Draw(img)

    width, height = img.size
    font_size = int(width * 0.06)

    try:
        font = ImageFont.truetype(FONT_MAP.get(tone), font_size)
    except:
        font = ImageFont.load_default()

    wrapped_text = textwrap.fill(caption, width=20)

    bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, align="center")
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (width - text_w) / 2
    y = height * 0.3

    draw.multiline_text(
        (x, y),
        wrapped_text,
        fill="black",
        font=font,
        align="center"
    )

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

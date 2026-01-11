from flask import Flask, request, send_file
from flask_cors import CORS
from ai_generator import generate_caption
from image_generator import create_poster
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/generate")
def generate():
    print("REQUEST RECEIVED")

    topic = request.args.get("topic", "College Event")
    tone = request.args.get("tone", "formal")
    template = request.args.get("template", "poster1.png")

    print("Params:", topic, tone, template)

    caption = generate_caption(topic, tone)
    print("Caption:", caption)

    image_buffer, saved_path = create_poster(caption, template, tone)
    print("Image saved at:", saved_path)

    return send_file(image_buffer, mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

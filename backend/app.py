from flask import Flask, request, send_file
from flask_cors import CORS
from ai_generator import generate_caption
from image_generator import create_poster

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend running with OpenAI"

@app.route("/generate")
def generate():
    topic = request.args.get("topic", "College Event")
    tone = request.args.get("tone", "formal")
    template = request.args.get("template", "poster1.png")

    caption = generate_caption(topic, tone)
    image = create_poster(caption, template, tone)

    return send_file(image, mimetype="image/png")

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=7860)

const BACKEND_URL = "https://anishrajigare-ai-poster-backend.hf.space";

function generatePoster() {
    const topic = document.getElementById("topic").value;
    const tone = document.getElementById("tone").value;
    const template = document.getElementById("template").value;

    const img = document.getElementById("resultImage");
    img.src = `${BACKEND_URL}/generate?topic=${encodeURIComponent(topic)}&tone=${tone}&template=${template}`;
}

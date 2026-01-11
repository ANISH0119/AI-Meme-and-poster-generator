const BACKEND_URL = "http://127.0.0.1:7860";

function generatePoster() {
    const topic = document.getElementById("topic").value.trim();
    const tone = document.getElementById("tone").value;
    const template = document.getElementById("template").value;

    const img = document.getElementById("resultImage");
    const status = document.getElementById("status");

    if (!topic || !tone || !template) {
        alert("Please fill all fields");
        return;
    }

    status.innerText = "Generating poster...";
    img.style.display = "none";

    const url =
        `${BACKEND_URL}/generate` +
        `?topic=${encodeURIComponent(topic)}` +
        `&tone=${tone}` +
        `&template=${template}`;

    img.onload = () => {
        status.innerText = "";
        img.style.display = "block";
    };

    img.onerror = () => {
        status.innerText = "Failed to generate poster";
        img.style.display = "none";
    };

    img.src = url;
}

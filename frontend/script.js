const BACKEND_URL = "https://anishrajigare-ai-poster-backend.hf.space/";



/* Load config.json and populate UI */
fetch("config.json")
    .then(response => response.json())
    .then(config => {

        if (document.getElementById("appTitle")) {
            document.getElementById("appTitle").innerText = config.app.title;
        }

        if (document.getElementById("appSubtitle")) {
            document.getElementById("appSubtitle").innerText = config.app.subtitle;
        }

        const toneSelect = document.getElementById("tone");
        if (toneSelect) {
            config.tones.forEach(tone => {
                const option = document.createElement("option");
                option.value = tone.value;
                option.text = tone.label;
                toneSelect.appendChild(option);
            });
        }

        const templateSelect = document.getElementById("template");
        if (templateSelect) {
            config.templates.forEach(template => {
                const option = document.createElement("option");
                option.value = template.file;
                option.text = template.label;
                templateSelect.appendChild(option);
            });
        }
    });

/* Navigate to result page */
function goToResult() {
    const topic = document.getElementById("topic").value;
    const tone = document.getElementById("tone").value;
    const template = document.getElementById("template").value;

    if (!topic) {
        alert("Please enter a topic");
        return;
    }

    const params = new URLSearchParams({
        topic: topic,
        tone: tone,
        template: template
    });

    window.location.href = `result.html?${params.toString()}`;
}

/* Load poster on result page */
if (window.location.pathname.includes("result.html")) {
    const params = new URLSearchParams(window.location.search);

    const topic = params.get("topic");
    const tone = params.get("tone");
    const template = params.get("template");

    const img = document.createElement("img");
    img.src = `${BACKEND_URL}/generate?topic=${topic}&tone=${tone}&template=${template}`;

    img.onload = function () {
        document.getElementById("loading").style.display = "none";
        document.getElementById("result").appendChild(img);
    };
}

/* Go back to input page */
function goBack() {
    window.location.href = "index.html";
}

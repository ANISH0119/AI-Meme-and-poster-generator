# 🎨 AI Meme & Poster Generator

A full-stack web application that generates **custom memes and posters** based on user input such as event/topic, tone, and visual template.
The system dynamically creates captions and overlays them on predefined poster templates to produce visually appealing outputs.

This project focuses on **end-to-end system integration, controlled AI text generation, and reliable deployment**.

---

## 🎯 Problem Statement

Creating posters or memes for events, announcements, or social media usually requires:

* Design skills
* Manual caption writing
* Repeated effort for different tones and formats

This process is **time-consuming and inconsistent**, especially for non-designers.

---

## 🧠 Proposed Solution

The AI Meme & Poster Generator automates this process by:

* Taking a simple text input (event/topic)
* Allowing users to select tone and template
* Automatically generating a caption
* Rendering the final poster image instantly

The system ensures **fast generation, consistency, and ease of use**.

---

## 🏗️ System Architecture

```text
User Input (Topic, Tone, Template)
 └─ Frontend (Vercel)
     └─ REST API Call
         └─ Backend (Flask)
             ├─ Caption Generation (Controlled NLG Logic)
             └─ Image Rendering (Pillow)
                 └─ Generated Poster
```

Each component is modular and independently testable.

---

## ⚡ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* Deployed on **Vercel**

### Backend

* Flask (Python)
* REST API architecture
* Deployed on **Hugging Face Spaces (Docker)**

### Image Processing

* Pillow (PIL)
* Dynamic text rendering
* Template-based poster generation

---

## ✨ Key Features

* Simple and intuitive UI
* Topic-based poster generation
* Multiple tone options (Funny, Formal, Motivational)
* Multiple poster templates
* Real-time image generation
* No page reloads required
* Graceful fallback logic for caption generation
* Fully deployed and shareable via public link

---

## 📁 Folder Structure (Simplified)

```text
backend/
├── app.py
├── ai_generator.py
├── image_generator.py
├── requirements.txt
├── Dockerfile
├── templates/
│   └── poster images
└── fonts/
    └── font files

frontend/
├── index.html
└── script.js
```

---

## 🛡️ Error Handling & Reliability

* Backend never crashes due to missing external APIs
* Safe fallback caption generation
* Invalid inputs handled gracefully
* Deployment-safe configuration using Docker
* Stateless API design

---

## 🌐 Live Demo

**Frontend (Vercel):**
[https://ai-meme-and-poster-generator.vercel.app/](https://ai-meme-and-poster-generator.vercel.app/)

**Backend (Hugging Face Spaces):**
[https://anishrajigare-ai-meme-poster-backend.hf.space/](https://anishrajigare-ai-meme-poster-backend.hf.space/)

> Note: The first request may take a few seconds on free-tier infrastructure due to container startup.

d next.

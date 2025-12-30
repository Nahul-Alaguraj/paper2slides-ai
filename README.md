**AI Paper-to-Slides Generator**

An end-to-end AI system that converts academic research papers (PDFs) into presentation-ready PowerPoint slides using Large Language Models (LLMs).

Upload a research paper → AI extracts key ideas → generates structured slides → downloads a real .pptx file.

Why This Project?

Academic research papers are:

Dense and time-consuming to read

Hard to summarize clearly

Even harder to convert into good presentations

This project automates that entire workflow, helping students, researchers, and professionals quickly understand and present research without manual effort.

What the System Does

Accepts a research paper PDF

Extracts and cleans text from the document

Uses an LLM to identify:

Problem statement

Methodology

Results

Conclusions

Limitations

Converts each section into presentation-ready bullet slides

Generates a downloadable PowerPoint (.pptx) file

Architecture Overview
PDF Upload (Frontend)
        ↓
FastAPI Backend
        ↓
PDF Parsing
        ↓
LLM Semantic Extraction
        ↓
Slide Bullet Generation
        ↓
PowerPoint (.pptx) Creation

Tech Stack
Backend

Python

FastAPI – API layer

Ollama (Local LLMs) – LLaMA 3.1 / Mistral

LangChain – LLM orchestration

python-pptx – PowerPoint generation

PyMuPDF / Unstructured – PDF parsing

Frontend

Next.js (App Router)

React

TypeScript

Tailwind CSS

✨ Key Features

📄 Upload research PDFs

🤖 Local LLM inference (no paid APIs)

🧠 Multi-stage AI reasoning pipeline

📊 Presentation-ready slide generation

💾 One-click PowerPoint download

🔐 Fully offline & privacy-friendly

📂 Project Structure
paper2slides-ai/
├── backend/
│   ├── main.py
│   ├── pdf_parse.py
│   ├── llm_extractor.py
│   ├── slide_generator.py
│   └── ppt_generator.py
├── frontend/
│   ├── app/
│   ├── components/
│   ├── package.json
│   └── tsconfig.json
├── .gitignore
└── README.md

⚙️ How to Run Locally
Prerequisites

Python 3.10+

Node.js 18+

Ollama installed and running

1️⃣ Start Ollama and pull a model
ollama pull llama3.1:8b


(or mistral:7b if preferred)

2️⃣ Backend setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

3️⃣ Frontend setup
cd frontend
npm install
npm run dev

4️⃣ Open the app

Visit:

http://localhost:3000


Upload a PDF → Generate slides → Download PPT 🎉

Example Use Cases

Students preparing seminar presentations

Researchers summarizing papers quickly

Educators creating lecture material

Professionals reviewing technical literature

What This Project Demonstrates

LLM orchestration beyond simple summarization

Document intelligence pipelines

Full-stack AI system design

Handling real-world LLM inconsistencies

Converting AI output into usable artifacts

Future Improvements

Speaker notes generation

Multiple slide themes

Image/figure extraction

Web-based slide previews (Reveal.js)

Multi-paper comparison

👤 Author

Nahul Alaguraj
AI / ML Enthusiast
GitHub: https://github.com/Nahul-Alaguraj

If you found this useful

Give the repo a ⭐ — it really helps!

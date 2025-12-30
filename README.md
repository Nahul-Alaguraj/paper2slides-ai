# Paper2Slides AI

> Transform research papers into presentation slides using local LLMs

An intelligent pipeline that converts academic PDFs into structured PowerPoint presentations using locally-hosted language models (Ollama). No cloud APIs, no costs, fully private.

---

## How It Works

```
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
```

---

## Tech Stack

### Backend
- **Python** - Core backend language
- **FastAPI** - High-performance API framework
- **Ollama** - Local LLM inference (LLaMA 3.1 / Mistral)
- **LangChain** - LLM orchestration
- **python-pptx** - PowerPoint generation
- **PyMuPDF / Unstructured** - PDF parsing

### Frontend
- **Next.js** - App Router framework
- **React** - UI library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first styling

---

##  Key Features

- 📄 Upload research PDFs
- 🤖 Local LLM inference (no paid APIs)
- 🧠 Multi-stage AI reasoning pipeline
- 📊 Presentation-ready slide generation
- 💾 One-click PowerPoint download
- 🔐 Fully offline & privacy-friendly

---

##  Project Structure

```
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
```

---

##  How to Run Locally

### Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- **Ollama** installed and running

---

### Start Ollama and pull a model

```bash
ollama pull llama3.1:8b
```

> You can also use `mistral:7b` or other compatible models.

---

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

---

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

### Open the App

Visit:

```
http://localhost:3000
```

Upload a PDF → Generate slides → Download PPT 🎉

---

## Example Use Cases

- **Students** preparing seminar presentations
- **Researchers** summarizing papers quickly
- **Educators** creating lecture material
- **Professionals** reviewing technical literature

---

## What This Project Demonstrates

- LLM orchestration beyond simple summarization
- Document intelligence pipelines
- Full-stack AI system design
- Handling real-world LLM inconsistencies
- Converting AI output into usable artifacts

---

## Future Improvements

- [ ] Speaker notes generation
- [ ] Multiple slide themes
- [ ] Image/figure extraction
- [ ] Web-based slide previews (Reveal.js)
- [ ] Multi-paper comparison

---

## Author

**Nahul Alaguraj**  
AI / ML Enthusiast

🔗 GitHub: [https://github.com/Nahul-Alaguraj](https://github.com/Nahul-Alaguraj)

---

## ⭐ If you found this useful

Give the repo a ⭐ — it really helps!

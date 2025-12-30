# backend/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
import aiofiles
from pdf_parse import extract_text_from_pdf
from llm_extractor import extract_paper_sections
from slide_generator import generate_slide_deck
from ppt_generator import generate_ppt
from fastapi.responses import FileResponse





app = FastAPI()

# Allow requests from Next.js dev server
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Backend is running!"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    save_path = os.path.join(UPLOAD_DIR, file.filename)

    async with aiofiles.open(save_path, "wb") as out_file:
        while content := await file.read(1024):
            await out_file.write(content)

    parsed = extract_text_from_pdf(save_path)

    sections = extract_paper_sections(parsed["full_text"])
    slides = generate_slide_deck(sections)

    return {
        "filename": file.filename,
        "slides": slides
    }
@app.post("/generate-ppt")
async def generate_ppt_endpoint(payload: dict):
    slides = payload.get("slides")

    if not slides or not isinstance(slides, list):
        return {"error": "Invalid slides data"}

    ppt_path = generate_ppt(slides)

    return FileResponse(
        ppt_path,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename="ai_generated_slides.pptx",
    )


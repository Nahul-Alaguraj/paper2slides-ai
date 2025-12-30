from pydantic import BaseModel
from typing import List

class Slide(BaseModel):
    title: str
    bullets: List[str]
    notes: str
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import json

def generate_slide(section_name: str, section_text: str) -> dict:
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a presentation expert. Convert academic content into concise slide bullets."
        ),
        (
            "human",
            """
Create ONE presentation slide from the following section.

Section: {section_name}

Rules:
- 3 to 5 bullet points
- Each bullet ≤ 12 words
- Clear, presentation-friendly language
- Avoid academic jargon

Text:
{section_text}

Return ONLY valid JSON:
{{
  "title": "string",
  "bullets": ["bullet 1", "bullet 2"],
  "notes": "speaker notes"
}}
"""
        )
    ])

    llm = ChatOllama(
        model="llama3.1:8b",
        temperature=0,
        timeout=120
    )

    response = llm.invoke(
        prompt.format(
            section_name=section_name,
            section_text=section_text
        )
    )

    raw = response.content.strip()

    # robust JSON extraction
    start = raw.find("{")
    end = raw.rfind("}") + 1
    return json.loads(raw[start:end])
def generate_slide_deck(sections: dict) -> dict:
    slides = []

    for section, text in sections.items():
        if not text or len(text.strip()) < 20:
            continue

        slide = generate_slide(section.capitalize(), text)
        slides.append(slide)

    return {"slides": slides}

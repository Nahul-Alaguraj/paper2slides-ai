# backend/llm_extractor.py

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
import json


class PaperSections(BaseModel):
    title: str = Field(description="Title of the paper")
    problem: str = Field(description="Problem statement")
    method: str = Field(description="Proposed method or approach")
    results: str = Field(description="Key experimental results")
    conclusion: str = Field(description="Conclusion of the paper")
    limitations: str = Field(description="Limitations or future work")


def extract_paper_sections(text: str) -> dict:
    """
    Extract semantic sections from a research paper using Ollama.
    """

    prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research assistant. "
        "Extract concise, presentation-ready content. "
        "Return ONLY valid JSON matching the given schema."
    ),
    (
        "human",
        """
Extract the following fields from the research paper text.

Schema:
{{
  "title": "string",
  "problem": "string",
  "method": "string",
  "results": "string",
  "conclusion": "string",
  "limitations": "string"
}}

Paper text:
{text}
"""
    )
])


    llm = ChatOllama(
        model="llama3.1:8b",
        temperature=0
    )

    chain = prompt | llm

    response = chain.invoke({"text": text[:12000]})

    # Ollama returns content as string
    raw_output = response.content.strip()

# ---- Robust JSON extraction ----
    start = raw_output.find("{")
    end = raw_output.rfind("}") + 1

    if start == -1 or end == -1:
        raise RuntimeError(f"No JSON found in LLM output:\n{raw_output}")

    json_str = raw_output[start:end]

    try:
        data = json.loads(json_str)
        return PaperSections(**data).dict()
    except Exception as e:
        raise RuntimeError(
            f"Failed to parse LLM JSON: {e}\n\nExtracted JSON:\n{json_str}"
        )


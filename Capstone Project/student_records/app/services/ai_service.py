import os
from ..config import settings
import openai


def summarize_student_prompt(student: dict) -> str:
    lines = [f"{k}: {v}" for k, v in student.items() if v is not None]
    prompt = "Create a concise, one-paragraph academic profile summary for the following student:\n\n"
    prompt += "\n".join(lines)
    prompt += "\n\nKeep it professional and about 2-3 sentences."
    return prompt


def call_openai_summary(student: dict) -> str:
    if not settings.OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not configured")
    openai.api_key = settings.OPENAI_API_KEY
    prompt = summarize_student_prompt(student)
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    return resp.choices[0].message.content.strip()

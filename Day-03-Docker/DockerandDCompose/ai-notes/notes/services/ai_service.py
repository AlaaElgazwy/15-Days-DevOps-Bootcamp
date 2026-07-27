import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_action_items(text: str) -> str:
    prompt = f"""
Extract only the action items from the following note.

Rules:
- Return one task per line.
- Do not explain anything.
- Do not use markdown.
- Keep tasks concise.

Note:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )

    return response.text.strip()
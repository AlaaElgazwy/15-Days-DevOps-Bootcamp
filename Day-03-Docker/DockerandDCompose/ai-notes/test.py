import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-flash-latest",
    "gemini-2.5-flash",
]

for model in models:
    try:
        response = client.models.generate_content(
            model=model,
            contents="Say hello"
        )
        print(f"✅ {model} works")
        print(response.text)
    except Exception as e:
        print(f"❌ {model}")
        print(e)
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN") or ""
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or ""
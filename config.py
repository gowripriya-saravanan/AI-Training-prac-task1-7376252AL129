"""Shared configuration and private computer-lab data."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "ollama").strip().lower()

if PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

elif PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")

elif PROVIDER == "huggingface":
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. "
        "Use ollama, groq or huggingface."
    )

if not API_KEY:
    raise SystemExit(
        f"No API key found for PROVIDER={PROVIDER}. "
        "Check your .env file."
    )

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


# -----------------------------------------
# PRIVATE COMPUTER LAB DATA
# -----------------------------------------

COMPUTERS = {
    "PC01": {
        "ram": 8,
        "storage": "512 GB SSD",
        "os": "Windows 11",
        "status": "Available"
    },

    "PC02": {
        "ram": 16,
        "storage": "512 GB SSD",
        "os": "Windows 11",
        "status": "Available"
    },

    "PC03": {
        "ram": 8,
        "storage": "1 TB HDD",
        "os": "Ubuntu",
        "status": "In Use"
    },

    "PC04": {
        "ram": 16,
        "storage": "1 TB SSD",
        "os": "Ubuntu",
        "status": "Available"
    },

    "PC05": {
        "ram": 32,
        "storage": "1 TB SSD",
        "os": "Windows 11",
        "status": "Maintenance"
    }
}


# -----------------------------------------
# QUESTIONS
# -----------------------------------------

QUESTIONS = [
    "Which computers are currently available?",

    "Which available computers have at least 16 GB RAM?",

    "How many GB of RAM are available in total on the available computers?",

    "I need a computer for Python and machine learning. "
    "Which available computer would be suitable?"
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | "
        f"model: {MODEL} ===\n"
    )
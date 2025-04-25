#from google import genai
import pandas as pd
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

REQUIRED_COLUMNS = ["company_name", "contact_name", "contacted_by", "contact_date", "notes"]

# Get the database URL from environment
#GEMINI_API = os.getenv("GEMINI_API")

#client = genai.Client(api_key = GEMINI_API) #access API key from .venv

def validate(file):
    REQUIRED_COLUMNS = [
        "Client Name",
        "Season",
        "Company",
        "Email/Linkedin/Insta",
        "Industry",
        "Website",
        "Reached Out?",
        "Response(Yes, No, Talking)",
        "Project Confirmed(Yes, No)",
        "Notes"
    ]

    data = pd.read_csv(file)

    # Add missing columns with empty string as default
    for col in REQUIRED_COLUMNS:
        if col not in data.columns:
            data[col] = ""

    data = data[REQUIRED_COLUMNS]

    return data



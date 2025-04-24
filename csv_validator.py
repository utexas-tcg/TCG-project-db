from google import genai 
import pandas as pd

client = genai.Client() #access API key from .venv

def validate(file):
    data = pd.read_csv(file)

    formatted_info = f"{row['EventName']} | {row['Performer_Name']} | {row['City']}, {row['State']} | {row['Venue']} | {row['Category']}"
    
    return

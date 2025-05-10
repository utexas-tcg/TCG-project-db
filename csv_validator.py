import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
import io

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API"))

REQUIRED_COLUMNS = [
    "Committee Member",
    "Client Name",
    "Season",
    "Company",
    "Contact Info",
    "Industry",
    "Website",
    "Reached Out?(Yes/No)",
    "Response(Yes/No/Talking)",
    "Project Confirmed(Yes/No)",
    "Notes"
]

# New: Create a properly formatted string
REQUIRED_COLUMNS_STRING = ",".join(REQUIRED_COLUMNS)

def validate(file):
    """Validate, clean, and split uploaded CSV using Gemini."""
    data = pd.read_csv(file)

    corrected_csv_text = gemini_audit_and_fix(data)

    with open("corrected_output.csv", "w", encoding="utf-8") as f:
        f.write(corrected_csv_text.strip())

    print('done with corrected csv file')

    # SAFER parsing
    cleaned_df = pd.read_csv(io.StringIO(corrected_csv_text.strip()), on_bad_lines="skip", engine="python")

    # Ensure required columns
    for col in REQUIRED_COLUMNS:
        if col not in cleaned_df.columns:
            cleaned_df[col] = ""

    cleaned_df = cleaned_df[REQUIRED_COLUMNS]

    cleaned_df["Reached Out?(Yes/No)"] = cleaned_df["Reached Out?(Yes/No)"].astype(str).str.strip().str.lower()

    reached_out_df = cleaned_df[cleaned_df["Reached Out?(Yes/No)"].str.lower() == "true"]
    print(reached_out_df)
    not_reached_out_df = cleaned_df[cleaned_df["Reached Out?(Yes/No)"].str.lower() != "true"]
    print(not_reached_out_df)

    return reached_out_df, not_reached_out_df


def gemini_audit_and_fix(data):
    """Use Gemini to reformat and clean the full CSV file into the required standardized format."""

    # Instead of .head(10), show the entire CSV content
    full_preview = data.to_csv(index=False)

    prompt = f"""
    You are a professional CSV data auditor and cleaner.

    You will be given full CSV data below. Some values may be missing and some rows may be completely blank or not relevant.
    You must clean and reformat the CSV according to these exact rules:

    CSV Data:
    {full_preview}

    Formatting Rules:
        - Only output valid CSV, starting immediately with the header row. No markdown, no explanations, no extra text.

    Header Columns (in exact order): {REQUIRED_COLUMNS_STRING}

    Rules for each column:

    1. Committee Member:
        - If exists, preserve the value.
        - If missing, fill with "N/A".

    2. Client Name:
        - This should be the *name of the individual person at the company* you reached out to.
        - If the cell contains a company name, move that to the "Company" column instead.
        - Acceptable formats: "John Doe", "Emily", "Michael Smith"
        - If a name cannot be extracted, set to "N/A".

    3. Season:
        - If exists, preserve.
        - If missing, fill with "N/A".

    4. Company:
        - Preserve.

    5. Contact Info:
        - Preserve.

    6. Industry:
        - Preserve if available.
        - If missing, determine what the industry is based on the company name and known industries.
        - Otherwise, fill with "Unknown Industry".

    7. Website:
        - Preserve.

    8. Reached Out?(Yes/No):
        - Normalize to only "True" or "False":
            - "yes", "y", "YES", "true", "True" → "True"
            - "no", "n", "NO", "false", "False" → "False"
        - If missing, default to "True".

    9. Response(Yes, No):
        - Normalize:
            - "yes", "y", "YES", "true", "True" → "True"
            - "no", "n", "NO", "false", "False" → "False"
        - If missing, default to "False".

    10. Project Confirmed(Yes, No):
        - Only mark "True" if confirmation ("yes", "y", "YES", "true", "True", "confirmed").
        - Otherwise, "False".

    11. Notes:
        - Preserve.

    General Rules:
        - Maintain original row order.
        - Match columns exactly as defined above.
        - Read each value carefully and apply rules individually.
        - Correct minor format issues silently but preserve real data.
        - Do not discard rows unless completely blank.

    Start your output immediately with this header: {REQUIRED_COLUMNS_STRING} 
    """



    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    response = model.generate_content(prompt)

    corrected_csv_text = response.text

    # Additional safety: Only keep content starting from "Client Name"
    if "Committee Member" in corrected_csv_text:
        corrected_csv_text = corrected_csv_text[corrected_csv_text.index("Committee Member"):]


    return corrected_csv_text


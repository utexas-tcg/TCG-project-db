import streamlit as st
import pandas as pd
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from datetime import datetime
from utils.utils import render_footer
from csv_validator import validate  # Import validate from csv_validate.py

def main():
    st.title("📤 Upload Outreach File\n---")

    db = SessionLocal()
    added = 0

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        df = validate(uploaded_file)  # Clean and standardize the uploaded file
        st.info("Previewing standardized file...")
        st.dataframe(df)

        if st.button("Submit to Database"):
            for _, row in df.iterrows():
                try:
                    entry = Outreach(
                        client_name=row['Client Name'],
                        season=row['Season'],
                        company=row['Company'],
                        email_linkedin_insta=row['Email/Linkedin/Insta'],
                        industry=row['Industry'],
                        website=row['Website'],
                        reached_out=row['Reached Out?'],
                        response=row['Response(Yes, No, Talking)'],
                        project_confirmed=row['Project Confirmed(Yes, No)'],
                        notes=row['Notes']
                    )
                    db.add(entry)
                    added += 1
                except Exception as e:
                    st.warning(f"Skipping row due to error: {e}")
            db.commit()
            st.success(f"{added} standardized rows successfully added to the database.")

    render_footer()

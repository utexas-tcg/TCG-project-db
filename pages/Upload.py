import streamlit as st
import pandas as pd
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from datetime import datetime
from utils.utils import render_footer

from csv_validator import validate

def main():
    st.title("Upload Outreach File")
    added = 0

    def handle_csv_upload(uploaded_file, db: Session, added):
        if uploaded_file:
            df = validate(uploaded_file)  # Clean and standardize the data

            if df is not None:
                for _, row in df.iterrows():
                    try:
                        entry = Outreach(
                            company_name=row['company_name'],
                            contact_name=row['contact_name'],
                            contacted_by=row['contacted_by'],
                            contact_date=datetime.strptime(row['contact_date'], "%Y-%m-%d").date(),
                            notes=row['notes']
                        )
                        db.add(entry)
                        added += 1
                    except Exception as e:
                        st.warning(f"Skipping row due to error: {e}")
                db.commit()
                st.success(f"{added} standardized rows added to the database.")

    db = SessionLocal()
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        handle_csv_upload(uploaded_file, db, added)

    render_footer()

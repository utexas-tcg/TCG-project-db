import streamlit as st
import pandas as pd
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from datetime import datetime
from utils.utils import render_footer
from csv_validator import validate  # Import validate from csv_validator.py

def main():
    st.title("📤 Upload Outreach File\n---")

    db = SessionLocal()
    added = 0
    skipped = 0

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        reached_out_df, not_reached_out_df = validate(uploaded_file)

        st.success("Standardized companies (Reached Out = True):")
        st.dataframe(reached_out_df)

        if not not_reached_out_df.empty:
            st.warning("These companies have NOT been reached out to and will not be added:")
            st.dataframe(not_reached_out_df)

        if st.button("Submit to Database"):
            for _, row in reached_out_df.iterrows():
                try:
                    if pd.isna(row['Client Name']) or pd.isna(row['Company']):
                        skipped += 1
                        continue  # Skip rows with missing Client Name or Company

                    existing_entry = db.query(Outreach).filter(
                        Outreach.company == row['Company'],
                        Outreach.client_name == row['Client Name']
                    ).first()

                    if existing_entry:
                        skipped += 1
                        continue  # Skip duplicates

                    entry = Outreach(
                        committee_member=row['Committee Member'],
                        client_name=row['Client Name'],
                        season=row['Season'],
                        company=row['Company'],
                        email_linkedin_insta=row['Email/Linkedin/Insta'],
                        industry=row['Industry'],
                        website=row['Website'],
                        reached_out=row['Reached Out?(Yes/No)'] == "true",
                        response=row['Response(Yes/No/Talking)'],
                        project_confirmed=row['Project Confirmed(Yes/No)'] == "true",
                        notes=row['Notes']
                    )
                    db.add(entry)
                    added += 1
                except Exception as e:
                    st.warning(f"Skipping row due to error: {e}")

            db.commit()
            st.success(f"{added} new rows added.")
            if skipped:
                st.info(f"{skipped} duplicate rows were skipped (already exist).")

    render_footer()
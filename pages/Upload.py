import streamlit as st
import pandas as pd
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from datetime import datetime
from utils.utils import render_footer
from csv_validator import validate  # Import validate from csv_validator.py

def prepare_display(df):
    df = df.fillna("N/A")
    bool_cols = ["Reached Out?(Yes/No)", "Response(Yes/No/Talking)", "Project Confirmed(Yes/No)"]
    for col in bool_cols:
        df[col] = df[col].astype(str).str.capitalize()
    return df

def main():
    st.title("Upload Outreach File\n---")

    db = SessionLocal()
    added = 0
    skipped = 0

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        reached_out_df, not_reached_out_df = validate(uploaded_file)

        # Clean display format for Streamlit
        reached_out_df_display = prepare_display(reached_out_df)
        not_reached_out_df_display = prepare_display(not_reached_out_df)

        st.dataframe(reached_out_df_display)

        if not not_reached_out_df.empty:
            st.warning("These companies have NOT been reached out to and will not be added:")
            st.dataframe(not_reached_out_df_display)

        if st.button("Submit to Database"):
            for _, row in reached_out_df.iterrows():
                try:
                    row = row.where(pd.notnull(row), None)  # <-- Converts NaN to None

                    # Skip only if BOTH Company AND Contact Info are missing
                    if row['Company'] is None or row['Contact Info'] is None:
                        skipped += 1
                        continue

                    # Checks previous entries in the database
                    existing_entry = db.query(Outreach).filter(
                        Outreach.company == row['Company'],
                        Outreach.contact_info == row['Contact Info']
                    ).first()

                    if existing_entry:
                        skipped += 1
                        continue  # Skip duplicates

                    entry = Outreach(
                        committee_member=row['Committee Member'],
                        client_name=row['Client Name'],
                        season=row['Season'],
                        company=row['Company'],
                        contact_info=row['Contact Info'],
                        industry=row['Industry'],
                        website=row['Website'],
                        reached_out=str(row['Reached Out?(Yes/No)']).strip().lower() == "true",
                        response=row['Response(Yes/No/Talking)'],
                        project_confirmed=str(row['Project Confirmed(Yes/No)']).strip().lower() == "true",
                        notes=row['Notes']
                    )
                    db.add(entry)
                    added += 1
                except Exception as e:
                    st.warning(f"Skipping row due to error: {e}")

            db.commit()
            st.success(f"{added} new rows added.")
            if skipped:
                st.info(f"{skipped} rows were skipped (duplicates or missing data).")


    render_footer()

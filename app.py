import streamlit as st
import pandas as pd
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from datetime import datetime
from csv_validator import validate

# Upload handler
def handle_csv_upload(file, db: Session):
    df = pd.read_csv(file)

    required_cols = {"company_name", "contact_name", "contacted_by", "contact_date", "notes"}
    if not required_cols.issubset(df.columns):
        st.error(f"CSV must contain these columns: {required_cols}")
        return

    added = 0
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
    st.success(f"{added} rows added to the database.")

#main app
def main():
    st.title("TCG Outreach Tracker")
    st.write("Upload a CSV of company outreach data to store it in the central database.")

    db = SessionLocal()

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        #call validate here so that all of our csv files are consistent
        handle_csv_upload(uploaded_file, db)

    st.markdown("---")
    if st.checkbox("View all outreach records"):
        records = db.query(Outreach).all()
        data = [{
            "Company": r.company_name,
            "Contact Name": r.contact_name,
            "Contacted By": r.contacted_by,
            "Date": r.contact_date,
            "Notes": r.notes
        } for r in records]
        st.dataframe(pd.DataFrame(data))

if __name__ == "__main__":
    main()

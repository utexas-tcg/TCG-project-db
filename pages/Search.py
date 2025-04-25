import streamlit as st
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from utils.utils import render_footer

def main():
    st.title("Search Companies")
    db: Session = SessionLocal()
    query = st.text_input("Search by company or member...")
    results = db.query(Outreach).all()

    for entry in results:
        if query.lower() in entry.company_name.lower() or query.lower() in entry.contacted_by.lower():
            with st.expander(f"📬 {entry.company_name} | Contacted by {entry.contacted_by} on {entry.contact_date}"):
                st.markdown(f"**Contact Name:** {entry.contact_name}")
                st.markdown(f"**Date Contacted:** {entry.contact_date}")
                st.markdown(f"**Notes:** {entry.notes}")

    render_footer()

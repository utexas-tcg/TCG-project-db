import streamlit as st
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from utils.utils import render_footer

def main():
    st.title("TCG Project Database")
    st.write("Welcome to the centralized system for managing company outreach.")
    
    # Add a divider
    st.markdown("---")
    
    db: Session = SessionLocal()

    results = db.query(Outreach).all()

    if not results:
        st.warning("No records found in the database.")
        render_footer()
        return

    # Display confirmed projects section
    confirmed_projects = [entry for entry in results if entry.project_confirmed]
    if confirmed_projects:
        st.subheader("✅ Past Projects")
        for i in range(0, len(confirmed_projects), 3):
            cols = st.columns(3)
            for j, entry in enumerate(confirmed_projects[i:i+3]):
                with cols[j]:
                    with st.expander(f"{entry.company or 'No Company Name'}"):
                        st.markdown(f"**TCG Member:** {entry.committee_member or 'N/A'}")
                        st.markdown(f"**Client Name:** {entry.client_name or 'N/A'}")
                        st.markdown(f"**Season:** {entry.season or 'N/A'}")
                        st.markdown(f"**Contact Info:** {entry.contact_info or 'N/A'}")
                        st.markdown(f"**Industry:** {entry.industry or 'N/A'}")
                        st.markdown(f"**Website:** {entry.website or 'N/A'}")
                        st.markdown(f"**Reached Out:** {entry.reached_out}")
                        st.markdown(f"**Response:** {entry.response}")
                        st.markdown(f"**Project Confirmed:** {entry.project_confirmed}")
                        st.markdown(f"**Notes:** {entry.notes or 'N/A'}")
        st.markdown("---")

  # Search functionality from Search.py
    st.subheader("🔍 Search Outreach Records")
    
    query = st.text_input("Search by Company or Client Name...").strip().lower()

    # Filter results based on query
    filtered = []
    for entry in results:
        # Handle None values by converting to empty strings before calling lower()
        company = entry.company.lower() if entry.company else ""
        contact_info = entry.contact_info.lower() if entry.contact_info else ""
        client_name = entry.client_name.lower() if entry.client_name else ""
        
        if (
            query in company
            or query in contact_info
            or query in client_name
        ):
            filtered.append(entry)

    if not filtered:
        st.info("No matches found for your query.")
    else:
        # Show cards in rows of 3
        for i in range(0, len(filtered), 3):
            cols = st.columns(3)
            for j, entry in enumerate(filtered[i:i+3]):
                with cols[j]:
                    with st.expander(f"{entry.company or 'No Company Name'}"):
                        st.markdown(f"**TCG Member:** {entry.committee_member or 'N/A'}")
                        st.markdown(f"**Client Name:** {entry.client_name or 'N/A'}")
                        st.markdown(f"**Season:** {entry.season or 'N/A'}")
                        st.markdown(f"**Contact Info:** {entry.contact_info or 'N/A'}")
                        st.markdown(f"**Industry:** {entry.industry or 'N/A'}")
                        st.markdown(f"**Website:** {entry.website or 'N/A'}")
                        st.markdown(f"**Reached Out:** {entry.reached_out}")
                        st.markdown(f"**Response:** {entry.response}")
                        st.markdown(f"**Project Confirmed:** {entry.project_confirmed}")
                        st.markdown(f"**Notes:** {entry.notes or 'N/A'}")

    render_footer()

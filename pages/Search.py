import streamlit as st
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from utils.utils import render_footer

def main():
    st.title("🔍 Search Outreach Records\n---")
   #st.markdown("# )

    db: Session = SessionLocal()
    query = st.text_input("Search by Company or Contact Info (Email/LinkedIn/Insta)...").strip().lower()

    results = db.query(Outreach).all()

    if not results:
        st.warning("No records found in the database.")
        render_footer()
        return

    # Filter results based on query
    filtered = []
    for entry in results:
        if (
            query in entry.company.lower()
            or query in entry.email_linkedin_insta.lower()
            or query in entry.client_name.lower()
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
                    with st.expander(f"{entry.company}"):
                        st.markdown(f"**Client Name:** {entry.client_name}")
                        st.markdown(f"**Season:** {entry.season}")
                        st.markdown(f"**Email/LinkedIn/Insta:** {entry.email_linkedin_insta}")
                        st.markdown(f"**Industry:** {entry.industry}")
                        st.markdown(f"**Website:** {entry.website}")
                        st.markdown(f"**Reached Out?** {entry.reached_out}")
                        st.markdown(f"**Response:** {entry.response}")
                        st.markdown(f"**Project Confirmed:** {entry.project_confirmed}")
                        st.markdown(f"**Notes:** {entry.notes}")

    render_footer()

import streamlit as st
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from utils.utils import render_footer
from industry_sorter import sort_industries

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
    
    # Search bar first, full width
    query = st.text_input("Search by Company or Client Name...").strip().lower()
    
    # Filters section
    st.write("Filters")
    show_filters = st.checkbox("Show advanced filters")
    
    # Advanced filters
    if show_filters:
        filter_cols = st.columns(2)
        
        with filter_cols[0]:
            # Get unique values for committee members
            committee_members = sorted(list(set(entry.committee_member for entry in results if entry.committee_member)))
            committee_members = ["All"] + committee_members
            selected_member = st.selectbox("TCG Member", committee_members)
            
            # Get unique values for industries and group similar ones
            all_industries = [entry.industry for entry in results if entry.industry]
            grouped_industries = sort_industries(all_industries)
            industries = ["All"] + sorted(grouped_industries.keys())
            selected_industry = st.selectbox("Industry", industries)
        
        with filter_cols[1]:
            # Get unique values for seasons
            seasons = sorted(list(set(entry.season for entry in results if entry.season)))
            seasons = ["All"] + seasons
            selected_season = st.selectbox("Season", seasons)
            
            # Response filter - only Yes/No
            responses = ["All", "Yes", "No"]
            selected_response = st.selectbox("Response", responses)

    # Filter results based on query and filters
    filtered = []
    for entry in results:
        # Handle None values by converting to empty strings before calling lower()
        company = entry.company.lower() if entry.company else ""
        contact_info = entry.contact_info.lower() if entry.contact_info else ""
        client_name = entry.client_name.lower() if entry.client_name else ""
        
        # Text search condition
        text_match = (
            query in company
            or query in contact_info
            or query in client_name
        )
        
        # If advanced filters are not shown, only use text search
        if not show_filters:
            if text_match:
                filtered.append(entry)
            continue
            
        # Filter by committee member
        member_match = True
        if selected_member != "All":
            member_match = entry.committee_member == selected_member
            
        # Filter by industry - check if entry's industry belongs to the selected group
        industry_match = True
        if selected_industry != "All":
            if entry.industry in grouped_industries.get(selected_industry, []):
                industry_match = True
            else:
                industry_match = False
            
        # Filter by season
        season_match = True
        if selected_season != "All":
            season_match = entry.season == selected_season
            
        # Filter by response - only Yes/No
        response_match = True
        if selected_response != "All":
            if selected_response == "Yes":
                response_match = entry.response == True
            elif selected_response == "No":
                response_match = entry.response == False
        
        # Add to filtered list if all conditions match
        if text_match and member_match and industry_match and season_match and response_match:
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

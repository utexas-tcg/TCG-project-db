import streamlit as st
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach
from utils.utils import render_footer
#from streamlit.runtime.scriptrunner import rerun

def main():
    st.title("Edit Outreach Records\n---")

    db: Session = SessionLocal()
    
    # Search functionality
    query = st.text_input("Search by Company or Client Name...").strip().lower()
    
    if query:
        # Filter results based on query
        results = db.query(Outreach).filter(
            (Outreach.company.ilike(f"%{query}%")) | 
            (Outreach.client_name.ilike(f"%{query}%"))
        ).all()
        
        if not results:
            st.info("No matches found for your query.")
        else:
            st.success(f"Found {len(results)} matching records")
            
            # Display each record with edit capability
            for i, entry in enumerate(results):
                with st.expander(f"{entry.company} - {entry.committee_member}"):
                    with st.form(key=f"edit_form_{i}"):
                        st.subheader("Edit Record")
                        
                        # Create form fields with current values
                        committee_member = st.text_input("TCG Member", value=entry.committee_member or "")
                        client_name = st.text_input("Client Name", value=entry.client_name or "")
                        season = st.text_input("Season", value=entry.season or "")
                        company = st.text_input("Company", value=entry.company or "")
                        contact_info = st.text_input("Contact Info", value=entry.contact_info or "")
                        industry = st.text_input("Industry", value=entry.industry or "")
                        website = st.text_input("Website", value=entry.website or "")
                        reached_out = st.checkbox("Reached Out?", value=entry.reached_out)
                        
                        # Change response to a simple checkbox
                        response = st.checkbox("Response (Yes/No)", value=entry.response)
                        
                        project_confirmed = st.checkbox("Project Confirmed", value=entry.project_confirmed)
                        notes = st.text_area("Notes", value=entry.notes or "", height=100)
                        
                        # Submit button for this form
                        submitted = st.form_submit_button("Save Changes")
                        
                        if submitted:
                            try:
                                # Update the entry with new values
                                entry.committee_member = committee_member
                                entry.client_name = client_name
                                entry.season = season
                                entry.company = company
                                entry.contact_info = contact_info
                                entry.industry = industry
                                entry.website = website
                                entry.reached_out = reached_out
                                entry.response = response
                                entry.project_confirmed = project_confirmed
                                entry.notes = notes
                                
                                # Commit changes to database
                                db.commit()
                                st.success("Record updated successfully!")
                            except Exception as e:
                                st.error(f"Error updating record: {e}")
                                db.rollback()
                
                    # Add delete button outside the form but inside the expander# Add delete button outside the form but inside the expander
                    if st.button(f"🗑️ Delete this record", key=f"delete_btn_{i}"):
                        try:
                            db.delete(entry)
                            db.commit()
                            st.success("Record deleted successfully!")
                            #rerun()
                        except Exception as e:
                            st.error(f"Error deleting record: {e}")
                            db.rollback()
    
    render_footer() 
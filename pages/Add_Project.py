import streamlit as st
from add_project import add_project

def main():
    st.title("Add New Project")
    st.write("Fill in the details below to add a new project.")

    company = st.text_input("Company")
    client_name = st.text_input("Client Name")
    committee_member = st.text_input("TCG Member")
    pm = st.text_input("PM")
    advisor = st.text_input("Advisor")
    member = st.text_input("Member")
    season = st.text_input("Season")
    contact_info = st.text_input("Contact Info")
    industry = st.text_input("Industry")
    website = st.text_input("Website")
    reached_out = st.checkbox("Reached Out")
    project_confirmed = st.checkbox("Project Confirmed")
    response = st.checkbox("Response")
    notes = st.text_area("Notes")
    

    if st.button("Add Project"):
        project = add_project(
            committee_member=committee_member,
            client_name=client_name,
            season=season,
            company=company,
            contact_info=contact_info,
            industry=industry,
            website=website,
            reached_out=reached_out,
            project_confirmed=project_confirmed,
            response=response,
            notes=notes,
            pm=pm,
            advisor=advisor,
            member=member
        )
        st.success(f"Project added: {project.company}")

if __name__ == "__main__":
    main() 
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from db.connect import SessionLocal
from db.models import Outreach

# Load environment variables
load_dotenv()

def add_project(committee_member, client_name, season, company, contact_info, industry, website, reached_out, project_confirmed, response, notes, pm=None, advisor=None, member=None):
    db: Session = SessionLocal()
    new_project = Outreach(
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
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    db.close()
    return new_project

if __name__ == "__main__":
    # Example usage
    project = add_project(
        committee_member="John Doe",
        client_name="Example Client",
        season="2023",
        company="Example Company",
        contact_info="contact@example.com",
        industry="Technology",
        website="www.example.com",
        reached_out=True,
        project_confirmed=True,
        response=True,
        notes="This is a test project.",
        pm="Jane Smith",
        advisor="Dr. Smith",
        member="Alice Johnson"
    )
    print(f"Added project: {project.company}") 
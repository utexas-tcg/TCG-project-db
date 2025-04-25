from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from db.connect import engine

# Base class for models
Base = declarative_base()

# Define table schema
class Outreach(Base):
    __tablename__ = "outreach2"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)
    season = Column(String)
    company = Column(String, index=True)
    email_linkedin_insta = Column(String)
    industry = Column(String)
    website = Column(String)
    reached_out = Column(String)
    response = Column(String)
    project_confirmed = Column(String)
    notes = Column(String)

# Create the table(s)
Base.metadata.create_all(bind=engine)

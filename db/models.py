from sqlalchemy import Column, Integer, String, Date, Boolean
from db.connect import Base, engine

# Define table schema
class Outreach(Base):
    __tablename__ = "outreach"

    id = Column(Integer, primary_key=True, index=True)
    committee_member = Column(String)
    pm = Column(String, nullable=True)
    members = Column(String, nullable=True)
    advisor = Column(String, nullable=True)
    client_name = Column(String)
    season = Column(String)
    company = Column(String, index=True)
    contact_info = Column(String)
    industry = Column(String)
    website = Column(String)
    reached_out = Column(Boolean)
    project_confirmed = Column(Boolean)
    response = Column(Boolean)
    notes = Column(String)
    

# Create the table(s)
Base.metadata.create_all(bind=engine)

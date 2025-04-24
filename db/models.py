from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from db.connect import engine

# Base class for models
Base = declarative_base()

# Define table schema
class Outreach(Base):
    __tablename__ = "outreach"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    contact_name = Column(String)
    contacted_by = Column(String, index=True)
    contact_date = Column(Date)
    notes = Column(String)

# Create the table(s)
Base.metadata.create_all(bind=engine)

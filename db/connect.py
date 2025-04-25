from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get the database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

print("DB URL:", DATABASE_URL)

# Create the engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

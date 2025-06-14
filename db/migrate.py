import os
import sys
from sqlalchemy import create_engine, text

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connect import DATABASE_URL

def add_new_columns():
    engine = create_engine(DATABASE_URL)
    
    # SQL statements to add new columns
    alter_statements = [
        "ALTER TABLE outreach ADD COLUMN IF NOT EXISTS pm TEXT;",
        "ALTER TABLE outreach ADD COLUMN IF NOT EXISTS members TEXT;",
        "ALTER TABLE outreach ADD COLUMN IF NOT EXISTS advisor TEXT;"
    ]
    
    try:
        with engine.connect() as connection:
            for statement in alter_statements:
                connection.execute(text(statement))
            connection.commit()
    except Exception as e:
        pass

if __name__ == "__main__":
    add_new_columns() 
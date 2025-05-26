from lib.db.connection import get_connection
from lib.db.seed import seed_database
import os

def setup_database():
    schema_path = os.path.join(os.path.dirname(__file__), '../lib/db/schema.sql')
    with open(schema_path, 'r') as f:
        schema = f.read()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.executescript(schema)
        conn.commit()
        seed_database()
    finally:
        conn.close()

if __name__ == "__main__":
    setup_database()

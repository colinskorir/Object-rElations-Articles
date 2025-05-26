from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
import os

def seed_database():
    # Ensure schema is loaded before seeding
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r') as f:
        schema = f.read()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.executescript(schema)
        conn.commit()
        conn.execute("DELETE FROM articles;")
        conn.execute("DELETE FROM authors;")
        conn.execute("DELETE FROM magazines;")
        conn.commit()

        # Create authors
        alice = Author("Alice Smith")
        bob = Author("Bob Johnson")
        carol = Author("Carol White")

        # Create magazines
        tech_today = Magazine("Tech Today", "Tech")
        health_weekly = Magazine("Health Weekly", "Health")

        # Add articles
        alice.add_article(tech_today, "AI in 2025")
        alice.add_article(health_weekly, "Healthy Living with Tech")
        bob.add_article(tech_today, "Quantum Computing Advances")
        carol.add_article(health_weekly, "Nutrition Myths Busted")
        carol.add_article(tech_today, "The Future of Robotics")

        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Seeding failed: {e}")
    finally:
        conn.close()

import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_database

@pytest.fixture(autouse=True)
def setup_database():
    seed_database()

def test_author_creation():
    author = Author("Test Author")
    assert author.id is not None
    assert author.name == "Test Author"

def test_author_articles():
    author = Author("Test Author 2")
    mag = Magazine("Test Mag", "Tech")
    author.add_article(mag, "Test Article")
    assert len(author.articles()) == 1

def test_author_magazines():
    author = Author("Test Author 3")
    mag1 = Magazine("Mag1", "Tech")
    mag2 = Magazine("Mag2", "Health")
    author.add_article(mag1, "A1")
    author.add_article(mag2, "A2")
    mags = author.magazines()
    assert len(mags) == 2

def test_author_topic_areas():
    author = Author("Test Author 4")
    mag1 = Magazine("Mag3", "Tech")
    mag2 = Magazine("Mag4", "Health")
    author.add_article(mag1, "A3")
    author.add_article(mag2, "A4")
    topics = author.topic_areas()
    assert "Tech" in topics and "Health" in topics

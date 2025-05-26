import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.db.seed import seed_database

@pytest.fixture(autouse=True)
def setup_database():
    seed_database()

def test_magazine_creation():
    mag = Magazine("Test Mag", "Tech")
    assert mag.id is not None
    assert mag.name == "Test Mag"
    assert mag.category == "Tech"

def test_magazine_articles():
    mag = Magazine("Test Mag2", "Tech")
    author = Author("Test Author 5")
    author.add_article(mag, "Article 1")
    assert len(mag.articles()) == 1

def test_magazine_contributors():
    mag = Magazine("Test Mag3", "Tech")
    author1 = Author("Test Author 6")
    author2 = Author("Test Author 7")
    author1.add_article(mag, "Article 2")
    author2.add_article(mag, "Article 3")
    contributors = mag.contributors()
    assert len(contributors) == 2

def test_magazine_article_titles():
    mag = Magazine("Test Mag4", "Tech")
    author = Author("Test Author 8")
    author.add_article(mag, "Article 4")
    titles = mag.article_titles()
    assert "Article 4" in titles

def test_magazine_top_publisher():
    mag = Magazine.top_publisher()
    assert mag is not None

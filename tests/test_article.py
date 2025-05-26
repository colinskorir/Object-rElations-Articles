import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_database

@pytest.fixture(autouse=True)
def setup_database():
    seed_database()

def test_article_creation():
    author = Author("Test Author 9")
    mag = Magazine("Test Mag5", "Tech")
    article = Article("Test Article 5", author, mag)
    assert article.id is not None
    assert article.title == "Test Article 5"
    assert article.author.id == author.id
    assert article.magazine.id == mag.id

def test_article_find_by_id():
    author = Author("Test Author 10")
    mag = Magazine("Test Mag6", "Tech")
    article = Article("Test Article 6", author, mag)
    found = Article.find_by_id(article.id)
    assert found is not None
    assert found.title == "Test Article 6"

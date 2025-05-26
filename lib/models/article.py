from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine

class Article:
    def __init__(self, title, author, magazine, id=None):
        self._id = id
        self.title = title
        self.author = author
        self.magazine = magazine
        if id is None:
            self._save()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Article title must be a non-empty string.")
        self._title = value.strip()

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("magazine must be a Magazine instance.")
        self._magazine = value

    def _save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (self.title, self.author.id, self.magazine.id)
            )
            self._id = cursor.lastrowid
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            author = Author.find_by_id(row['author_id'])
            magazine = Magazine.find_by_id(row['magazine_id'])
            return cls(row['title'], author, magazine, row['id'])
        return None

    @staticmethod
    def _get_author_from_row(row):
        from lib.models.author import Author
        return Author.find_by_id(row['author_id'])

    @staticmethod
    def _get_magazine_from_row(row):
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(row['magazine_id'])

"""Entity book data model
"""

from datetime import date

from sqlalchemy import Column, String, Integer, Date

from core import DB


class Book(DB.Model):
    """Data model table book"""

    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, unique=True)
    synopsis = Column(String(500), nullable=False)
    number_of_pages = Column(Integer, nullable=False)
    author = Column(String(50), nullable=False)
    publisher = Column(String(50), nullable=False)
    language = Column(String(20), nullable=False)
    publication_date = Column(Date, default=date.today())

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __eq__(self, other):
        if self is None or other is None:
            return False

        return (
                self.title == other.title and
                self.synopsis == other.synopsis and
                self.number_of_pages == other.number_of_pages and
                self.author == other.author and
                self.publisher == other.publisher and
                self.language == other.language and
                self.publication_date == other.publication_date
        )

    def valid_update(self):
        """Verify if there's at least one field that is not None"""
        if (
                self.id or
                self.title or
                self.synopsis or
                self.number_of_pages or
                self.author or
                self.publisher or
                self.language or
                self.publication_date
        ):
            return True
        return False

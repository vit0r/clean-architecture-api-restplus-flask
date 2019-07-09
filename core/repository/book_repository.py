"""
This Module Provides advanced repository functionalities for Book Objects
"""
from core.entities import Book
from .base_repository import BaseRepository


class BookRepository(BaseRepository):
    """Book repository access"""
    def __init__(self):
        """Initialize values self.class"""
        super().__init__(Book)

    def __repr__(self):
        """Representation of class"""
        return '{}()'.format(self.__class__.__name__)

    @classmethod
    def find_by_title(cls, title):
        """Get book by title if exists"""
        return Book.query.filter(Book.title == title).first()

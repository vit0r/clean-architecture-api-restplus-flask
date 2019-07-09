"""This Module contains the Usecases - write business codes rules"""

from core.repository.book_repository import BookRepository
from . import AbstractBaseBookUseCase


class BookUseCase(AbstractBaseBookUseCase):
    """"This Class contains the App Usecases"""
    def __init__(self):
        """Init class values"""
        self.repository = BookRepository()

    def __repr__(self):
        """Representation of class"""
        return '{}()'.format(self.__class__.__name__)

    def find_by_id(self, book_id):
        """Find book by id"""
        if book_id <= 0:
            return None
        return self.repository.find_by_id(book_id)

    def find_all(self):
        """Find all books"""
        return self.repository.find_all()

    def find_by_title(self, title):
        """Find book by tilte"""
        return self.find_by_title(title)

    def create(self, data):
        """Create book if it doesn't exists"""
        found = self.repository.find_by_title(data.title)
        if not found:
            return self.repository.create(data)
        return False

    def update_or_patch(self, book_id, data):
        """Update book if exists"""
        found = self.repository.find_by_id(book_id)
        if found:
            return self.repository.update_or_patch(found, data)
        return False

    def delete(self, book_id):
        """Delete book if exists"""
        return self.repository.delete(book_id)

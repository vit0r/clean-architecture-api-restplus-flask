"""This Module implements the Abstract class to define signature for usecase methods"""
from abc import ABCMeta, abstractmethod


class AbstractBaseBookUseCase:
    """ Abstract Class for Book Use Case"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def __repr__(self):
        """Representation of class"""
        raise NotImplementedError('__repr__() book not implemented yet')

    @abstractmethod
    def find_by_id(self, book_id):
        """Find book by id"""
        raise NotImplementedError('find_by_id book not implemented yet')

    @abstractmethod
    def find_all(self):
        """Find all books"""
        raise NotImplementedError('find_all book not implemented yet')

    @abstractmethod
    def find_by_title(self, title):
        """Find book by tilte"""
        raise NotImplementedError('find_by_title not implemented yet')

    @abstractmethod
    def create(self, data):
        """Add a new book"""
        raise NotImplementedError('create book not implemented yet')

    @abstractmethod
    def update_or_patch(self, book_id, data):
        """Update or patch an existing book"""
        raise NotImplementedError('update_or_patch book not implemented yet')

    @abstractmethod
    def delete(self, book_id):
        """Delete a book"""
        raise NotImplementedError('delete book not implemented yet')

"""Adapter sinature for api methods
"""

from abc import ABCMeta, abstractmethod

__all__ = "AbstractBaseAdapter"


class AbstractBaseAdapter:
    """Abstract base class adapter"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def __repr__(self):
        """Representation for abstract class"""
        raise NotImplementedError("__repr__ not implemented yet")

    @abstractmethod
    def find_by_id(self, book_id):
        """Receive book by id"""
        raise NotImplementedError("find_one not implemented yet")

    @abstractmethod
    def find_all(self):
        """Receive all book by id"""
        raise NotImplementedError("find_all not implemented yet")

    @abstractmethod
    def create(self, data):
        """Create a new book"""
        raise NotImplementedError("create not implemented yet")

    @abstractmethod
    def update_or_patch(self, book_id, data):
        """Update or patch book data with id"""
        raise NotImplementedError("update not implemented yet")

    @abstractmethod
    def delete(self, book_id):
        """Delete book by id"""
        raise NotImplementedError("delete not implemented yet")

"""This Module Implements the Abstract class to repository methods"""

from abc import ABCMeta, abstractmethod

__all__ = "BaseRepository"


class AbstractBaseRepository:
    """Abstract class to repository methods"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def __repr__(self):
        """Representation class name"""
        raise NotImplementedError("__repr__(self) book not implemented yet")

    @abstractmethod
    def find_by_id(self, object_id):
        """Find book by id"""
        raise NotImplementedError("find_by_id(book_id) book not implemented yet")

    @abstractmethod
    def find_all(self):
        """Find all book"""
        raise NotImplementedError("find_all book not implemented yet")

    @abstractmethod
    def create(self, data):
        """Create new book"""
        raise NotImplementedError("create book not implemented yet")

    @abstractmethod
    def update_or_patch(self, old_data_model, new_data_model):
        """Update or path book"""
        raise NotImplementedError("update or patch book not implemented yet")

    @abstractmethod
    def delete(self, object_id):
        """Delete book by id"""
        raise NotImplementedError("delete book not implemented yet")

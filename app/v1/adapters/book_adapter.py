"""Book adapter and book schema"""

from datetime import date

from marshmallow import fields, validates, ValidationError, Schema, post_load

from core.adapters.base_adapter import BaseAdapter
from core.entities import Book
from core.usecases.book_usecase import BookUseCase


class BookSchema(Schema):
    """Define book schema contract"""

    def __repr__(self):
        """Representation of class"""
        return '{}()'.format(self.__class__.__name__)

    @post_load
    def to_book_model(self, data):
        """Create book model from book schema"""
        print('Create book model from data dict {}'.format(self.__dict__))
        return Book(**data)

    @classmethod
    @validates('title')
    def validate_title(cls, data):
        """Validate title property"""
        if len(data) > 50:
            raise ValidationError('Title must be less or eq than 50.')

    id = fields.Integer(required=False, allow_none=True)
    title = fields.Str(required=True, attribute='title')
    synopsis = fields.Str(required=True)
    number_of_pages = fields.Int(required=True)
    author = fields.Str(required=True)
    publisher = fields.Str(required=True)
    language = fields.Str(required=True)
    publication_date = fields.Date(default=date.today())


class BookAdapter(BaseAdapter):
    """Book adapter with crud methods"""

    def __init__(self):
        """Initialize class with book use case and book schema"""
        super().__init__(BookUseCase, BookSchema)

    def __repr__(self):
        """CLass representation"""
        return '{}()'.format(self.__class__.__name__)

"""
This module is responsible for translating the API I/O
"""

from marshmallow import ValidationError

from . import AbstractBaseAdapter


class BaseAdapter(AbstractBaseAdapter):
    """Base adapater for api contract"""

    def __init__(self, usecase, schema):
        self.usecase = usecase()
        self.schema = schema

    def __repr__(self):
        return '{}(entity, usecase)'.format(self.__class__.__name__)

    def find_by_id(self, book_id):
        book_found = self.usecase.find_by_id(book_id)
        if not book_found:
            return None
        dump, errors = self.schema().dump(book_found)
        print(errors)
        return dump

    def find_all(self):
        data_model = self.usecase.find_all()
        dump, errors = self.schema(many=True).dump(data_model)
        print(errors)
        return dump

    def create(self, data):
        has_created = False
        try:
            model_data, errors = self.schema().load(data)
            if not errors:
                has_created = self.usecase.create(model_data)
        except ValidationError as err:
            print(err.messages)
        return has_created

    def update_or_patch(self, book_id, data):
        has_updated = False
        try:
            model_data, errors = self.schema(partial=True).load(data)
            if model_data.valid_update() and not errors:
                has_updated = self.usecase.update_or_patch(book_id, model_data)
        except (ValidationError, TypeError) as err:
            if err is ValidationError:
                print(err.messages)

        return has_updated

    def delete(self, book_id):
        return self.usecase.delete(book_id)

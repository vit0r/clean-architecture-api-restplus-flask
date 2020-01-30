"""
This Module Provides Basic Repository Functionality
"""
from core.startup import DB
from sqlalchemy.exc import SQLAlchemyError

from . import AbstractBaseRepository


class BaseRepository(AbstractBaseRepository):
    """
    Base Repository Class with Basic methods which Book repository will inherit from.
    """

    def __init__(self, entity):
        self.__entity = entity

    def __repr__(self):
        "{}(entity)".format(self.__class__.__name__)

    def __getitem__(self, item):
        return self.__entity.query.get(item)

    def find_by_id(self, object_id):
        return self.__getitem__(object_id)

    def find_all(self):
        results = self.__entity.query.all()
        return results

    def create(self, data):
        committed = True
        try:
            DB.session.add(data)
            DB.session.commit()
        except SQLAlchemyError as ex:
            print(ex)
            DB.session.rollback()
            committed = True
        finally:
            DB.session.close()
        return committed

    def update_or_patch(self, old_data_model, new_data_model):
        committed = True
        try:
            new_data_model.id = old_data_model.id
            DB.session.merge(new_data_model)
            DB.session.commit()
        except SQLAlchemyError as ex:
            print(ex)
            DB.session.rollback()
            committed = False
        finally:
            DB.session.close()
        return committed

    def delete(self, object_id):
        committed = True
        try:
            data_model = self.__getitem__(object_id)
            DB.session.delete(data_model)
            DB.session.commit()
        except SQLAlchemyError as ex:
            print(ex)
            DB.session.rollback()
            committed = False
        finally:
            DB.session.close()
        return committed

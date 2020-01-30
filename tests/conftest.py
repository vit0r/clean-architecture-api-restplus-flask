""" This Module Contains The Hooks used in the Automated Tests"""
from os import environ

import pytest
from app import create_app
from core.startup import DB
from sqlalchemy.exc import SQLAlchemyError
from tests.mocked_books_formated import valid_book_list


@pytest.fixture(autouse=True, scope="session")
def setup():
    """ Run Before Test """
    print("\nPreparing tests for {}".format(environ["PYTEST_CURRENT_TEST"]))
    environ["ENVID"] = "test_v1.json"
    app_test = create_app()
    ctx = app_test.app_context()
    ctx.push()
    yield app_test
    print("\nFinalizing tests - {}".format(environ["PYTEST_CURRENT_TEST"]))
    environ.pop("ENVID")
    ctx.pop()


@pytest.fixture(autouse=True, scope="function")
def create_db():
    """need reset array for books because commit flush all objects books passed to add"""
    books = valid_book_list()
    try:
        DB.reflect()
        DB.drop_all()
        DB.create_all()
        for book in books:
            DB.session.add(book)
        DB.session.commit()
    except SQLAlchemyError as sae:
        print(sae)
    finally:
        pass
    DB.session.remove()  # include to close transactions

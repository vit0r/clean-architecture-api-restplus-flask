"""This Module contains the Book Repository Integration Tests """
import pytest
from core.entities import Book
from core.repository.book_repository import BookRepository
from tests.mocked_books_formated import (
    patched_title,
    valid_book,
    valid_book_list,
    valid_updated_book,
)


def test_book_repository_find_all_success():
    """Receive all books"""
    # Arrange
    #  There is no Arrange here. The memory DB is prepared in a fixture.
    #  See conftest.py to see how this is done.

    # Act
    all_books = BookRepository().find_all()

    # Assert
    assert all_books == valid_book_list()


def test_book_repository_find_id_valid_id_success():
    """Receive one book by id"""

    # Arrange
    book_id = 2
    # Act
    book_found = BookRepository().find_by_id(book_id)

    # Assert
    # Assert if the method returned something
    assert book_found is not None
    # Assert if the method returned what we wanted
    assert book_found.id == book_id


def test_book_repository_create_valid_book_success():
    """Should be create a new book"""
    # Our repository methods that don't return useful Data return a boolean variable
    # to verify success or failure of ORM operations. This makes testing simple and clean.

    book_created = BookRepository().create(valid_book())
    assert book_created


@pytest.mark.parametrize("book_id", [2])
def test_book_repository_delete_valid_id_success(book_id):
    """Should be delete one book by id"""
    # Arrange

    #   In this test, the arrange was done by using pytest mark.parametrize
    #   Testing Frameworks support many features that make developing tests easier and cleaner.

    # Act
    book_deleted = BookRepository().delete(book_id)
    # Assert
    assert book_deleted


def test_book_repository_update_valid_data_success():
    """Should update or patch """

    # It's a good practice to separate testing data from the actual tests. In this test,
    # valid_update_book is a method that returns valid data for the update_or_patch test.
    # We could simply out this data in arrange, but then our test would be difficult to read.
    # This approach also makes reusing this data in other tests easier.

    # Arrange

    valid_update_book_data = valid_updated_book()
    book_id = valid_update_book_data.id
    book_to_update = BookRepository().find_by_id(book_id)

    # Act
    book_updated = BookRepository().update_or_patch(
        book_to_update, valid_update_book_data
    )

    # Assert
    assert book_updated

    updated_book = BookRepository().find_by_id(book_id)

    assert updated_book == valid_update_book_data


# A few more tests with different forms of parametrization.
@pytest.mark.parametrize("book_patch", [(Book(title=patched_title()))])
def test_book_repository_patch_valid_data_success_parametrize_example(book_patch):
    """Should be update or patch one book by id"""
    book_to_update = BookRepository().find_by_id(3)

    book_updated = BookRepository().update_or_patch(book_to_update, book_patch)

    updated_book = BookRepository().find_by_id(3)
    assert book_updated
    assert updated_book.title == patched_title()


def test_book_repository_find_id_invalid_id_not_found():
    """Error to find a non existing book"""
    book_id = 3202
    book_found = BookRepository().find_by_id(book_id)
    assert book_found is None


@pytest.mark.parametrize("book_id", [32200])
def test_book_repository_delete_invalid_id_error(book_id):
    """Should error to delete a non existing book"""
    book_deleted = BookRepository().delete(book_id)
    assert not book_deleted

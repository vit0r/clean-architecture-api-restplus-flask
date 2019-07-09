""" This Module Contains the Book Usecases Integration tests"""

from core.usecases.book_usecase import BookUseCase
from tests.mocked_books_formated import valid_book_list


# <editor-fold desc="tests-success">

# The Following test is a Anti-Pattern. BookUseCase.find_all just call repository find_all,
# which we already tested.
# There's no need to test a method that only calls another method.

def test_book_find_all():
    """Receive all books"""
    all_books = BookUseCase().find_all()
    assert all_books == valid_book_list()


# The next test is another Anti-Pattern. We already covered the Usecase business rules in unit
#  tests, and we already covered the DB integration with the repository class integration tests.
# Why do we have to test the UseCase business rules again?
# Planning Tests is very important to avoid the development of unnecessary tests.


def test_book_usecases_find_id_valid_id_success():
    """Receive one book by id"""
    # Arrange
    book_id = 2
    # Act
    book_found = BookUseCase().find_by_id(book_id)

    # Assert
    assert book_found is not None
    assert book_found.id == book_id

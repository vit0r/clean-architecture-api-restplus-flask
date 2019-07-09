""" This module contains usecase unit tests """

from core.repository.book_repository import BaseRepository
from core.repository.book_repository import BookRepository
from core.usecases.book_usecase import BookUseCase

from tests.mocked_books_formated import valid_book_list, valid_updated_book, valid_book


# BookUseCase adds a new business rule to the find_by_id method.
# Thus, we need to create new tests to evaluate it.

def test_book_usecase_find_by_id_valid_id(mocker):
    """Should return the mocked book"""
    # Arrange - here we are mocking the call for another method.
    mocker.patch('core.repository.book_repository.BookRepository.find_by_id')
    mocked_result = valid_book()
    BookRepository.find_by_id.return_value = mocked_result
    invalid_book_id = 1

    # Act
    book_found = BookUseCase().find_by_id(invalid_book_id)

    # Assert
    assert book_found == mocked_result


def test_book_usecase_find_by_id_invalid_id(mocker):
    """Should return None"""
    # Arrange
    mocker.patch('core.repository.book_repository.BookRepository.find_by_id')
    BookRepository.find_by_id.return_value = valid_book()
    invalid_book_id = 0

    # Act
    book_found = BookUseCase().find_by_id(invalid_book_id)

    # Assert
    assert book_found is None


# The same is true for Create and update methods, so we need to test their business rules as well.


def test_book_use_case_create_valid_book_success(mocker):
    """ creation method should return Success   """
    # Arrange
    mocker.patch('core.repository.book_repository.BookRepository.find_by_title')
    BookRepository.find_by_title.return_value = None

    book_to_create = valid_book()
    mocker.patch('core.repository.base_repository.BaseRepository.create')
    BaseRepository.create.return_value = True

    # Act
    created_successfully = BookUseCase().create(book_to_create)

    # Asert
    assert created_successfully


def test_book_use_case_create_existing_book_fail(mocker):
    """ should return false when book create fails """

    # Arrange
    mocker.patch('core.repository.book_repository.BookRepository.find_by_title')
    existing_book = valid_book_list()[0]
    BookRepository.find_by_title.return_value = existing_book

    book_to_create = existing_book
    mocker.patch('core.repository.base_repository.BaseRepository.create')
    BaseRepository.create.return_value = False

    # Act
    created_successfully = BookUseCase().create(book_to_create)

    # Asert
    assert not created_successfully


def test_book_use_case_update_or_patch_existing_book_succeed(mocker):
    """ Should return true when updating a existing book """

    # Arrange
    mocker.patch('core.repository.book_repository.BookRepository.find_by_id')
    existing_book = valid_book_list()[2]
    BookRepository.find_by_id.return_value = existing_book

    mocker.patch('core.repository.book_repository.BookRepository.update_or_patch')
    updated_book = valid_updated_book()
    BookRepository.update_or_patch.return_value = True

    # Act
    updated_successfully = BookUseCase().update_or_patch(updated_book.id, updated_book)

    # Assert
    assert updated_successfully


def test_book_use_case_update_or_patch_nonexistent_book_fail(mocker):
    """ should return false when updating an invalid book """

    # Arrange
    mocker.patch('core.repository.book_repository.BookRepository.find_by_id')
    existing_book = None
    BookRepository.find_by_id.return_value = existing_book

    mocker.patch('core.repository.book_repository.BookRepository.update_or_patch')
    updated_book = valid_updated_book()
    updated_book.id = 1
    BookRepository.update_or_patch.return_value = False

    # Act
    updated_successfully = BookUseCase().update_or_patch(updated_book.id, updated_book)

    # Assert
    assert not updated_successfully

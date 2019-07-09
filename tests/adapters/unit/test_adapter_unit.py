""" This Module contains the adapter unit tests"""

from app.v1.adapters.book_adapter import BookAdapter
from core.usecases.book_usecase import BookUseCase
from tests.mocked_books_json import VALID_BOOK, INCOMPLETE_BOOK, INVALID_UPDATE_DATA


def test_book_adapter_create_valid_book_success(mocker):
    """Book is created when valid json is inputed"""
    mocker.patch('core.usecases.book_usecase.BookUseCase.create')
    BookUseCase.create.return_value = True

    book_created = BookAdapter().create(VALID_BOOK)

    assert book_created


def test_book_adapter_create_invalid_book_fail(mocker):
    """Book is created when valid json creation is inputted"""
    mocker.patch('core.usecases.book_usecase.BookUseCase.create')
    BookUseCase.create.return_value = True

    book_created = BookAdapter().create(INCOMPLETE_BOOK)

    assert not book_created


def test_update_or_patch_valid_book_success(mocker):
    """Book is created when valid json update is inputted"""
    mocker.patch('core.usecases.book_usecase.BookUseCase.update_or_patch')
    BookUseCase.update_or_patch.return_value = True
    book_id = 5

    book_updated = BookAdapter().update_or_patch(book_id, INCOMPLETE_BOOK)

    assert book_updated


def test_update_or_patch_valid_book_fail(mocker):
    """Book is created when valid json update is inputted"""
    mocker.patch('core.usecases.book_usecase.BookUseCase.update_or_patch')
    BookUseCase.update_or_patch.return_value = True
    book_id = 5

    book_updated = BookAdapter().update_or_patch(book_id, INVALID_UPDATE_DATA)

    assert not book_updated

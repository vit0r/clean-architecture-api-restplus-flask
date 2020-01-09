"""
Unit tests to book api
test name pattern: # test_[class]_[method]_[scenario to test]_[expected result]
"""

import pytest
from app.v1.adapters.book_adapter import BookAdapter
from tests.mocked_books_json import INVALID_UPDATE_DATA, VALID_BOOK, VALID_BOOK_LIST

# <editor-fold desc="tests-endpoints">

__BASE_URL = "/api/{}/book/"
__BASE_URL_ID = "/api/{}/book/{}"


# </editor-fold>

# <editor-fold desc="tests-success">


def test_book_find_all_success(setup, mocker):
    """Receive all books"""
    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.find_all")
    BookAdapter.find_all.return_value = VALID_BOOK_LIST
    api_version = setup.config.get("BLUEPRINTS").get("version")

    test_client = setup.test_client()
    response = test_client.get(__BASE_URL.format(api_version))

    assert response.status_code == 200
    assert response.json == VALID_BOOK_LIST


@pytest.mark.parametrize("book_id", [3])
def test_bookitems_find_by_id_valid_id_success(setup, mocker, book_id):
    """Receive one book has id 9"""
    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.find_by_id")
    BookAdapter.find_by_id.return_value = VALID_BOOK

    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    response = test_client.get(__BASE_URL_ID.format(api_version, book_id))

    assert response.status_code == 200
    assert response.json == VALID_BOOK


@pytest.mark.parametrize("book_id", [500])
def test_bookitems_find_by_id_invalid_id_fail(setup, mocker, book_id):
    """Receive one book has id 9"""
    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.find_by_id")
    BookAdapter.find_by_id.return_value = None

    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    response = test_client.get(__BASE_URL_ID.format(api_version, book_id))

    assert response.status_code == 404


@pytest.mark.parametrize("book_id", [8])
def test_book_delete_valid_id_success(setup, mocker, book_id):
    """Return 204 if book was deleted"""

    # Arrange
    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.delete")
    BookAdapter.delete.return_value = True
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    # Act
    response = test_client.delete(__BASE_URL_ID.format(api_version, book_id))
    # Assert
    assert response.status_code == 204


@pytest.mark.parametrize("book_id", [320])
def test_book_delete_invalid_id_fail(setup, mocker, book_id):
    """Receive one book has id 8"""

    # Arrange
    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.delete")
    BookAdapter.delete.return_value = False
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    # Act
    response = test_client.delete(__BASE_URL_ID.format(api_version, book_id))
    # Assert
    assert response.status_code == 500


def test_bookitems_update_book_valid_book_success(setup, mocker):
    """Receive one book has id 3"""

    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.update_or_patch")
    BookAdapter.update_or_patch.return_value = True

    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    book_id = 5
    book_update = VALID_BOOK

    response = test_client.put(
        __BASE_URL_ID.format(api_version, book_id), json=book_update
    )

    assert response.status_code == 204


def test_bookitems_update_book_invalid_book_fail(setup, mocker):
    """Receive one book has id 3"""

    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.update_or_patch")
    BookAdapter.update_or_patch.return_value = False
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    book_id = 51
    book_update = INVALID_UPDATE_DATA

    response = test_client.put(
        __BASE_URL_ID.format(api_version, book_id), json=book_update
    )

    assert response.status_code == 500


def test_book_create_book_title_book34_success(setup, mocker):
    """create a book has title book34"""

    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.create")
    BookAdapter.create.return_value = True
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()

    response = test_client.post(__BASE_URL.format(api_version), json=VALID_BOOK)

    assert response.status_code == 201


def test_book_create_book_title_book34_fail(setup, mocker):
    """create a book has title book34"""

    mocker.patch("app.v1.adapters.book_adapter.BookAdapter.create")
    BookAdapter.create.return_value = False
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()

    response = test_client.post(__BASE_URL.format(api_version), json=VALID_BOOK)

    assert response.status_code == 500


# </editor-fold>

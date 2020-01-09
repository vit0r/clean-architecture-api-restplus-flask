"""
Component tests to book api
test name pattern: # test_[class]_[method]_[scenario to test]_[expected result]
"""
import pytest
from app.v1.adapters.book_adapter import BookSchema
from core.entities import Book
from tests.mocked_books_formated import valid_book_list
from tests.mocked_books_json import VALID_BOOK

# <editor-fold desc="tests-endpoints">

__BASE_URL = "/api/{}/book/"
__BASE_URL_ID = "/api/{}/book/{}"


# </editor-fold>

# <editor-fold desc="tests-success">


def test_book_find_all_receive_all_books_success(setup):
    """Receive all books"""
    # Arrange
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()

    # Act
    response = test_client.get(__BASE_URL.format(api_version))

    # Assert
    assert response.status_code == 200

    books, errors = BookSchema(many=True).load(response.json)
    assert not errors
    assert books == valid_book_list()


@pytest.mark.parametrize("book_id", [5])
def test_bookitems_find_by_id_receive_correct_book(setup, book_id):
    """Receive one book has id 8"""
    # Arrange
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()

    # Act
    response = test_client.get(__BASE_URL_ID.format(api_version, book_id))

    # Assert
    assert response.status_code == 200
    assert Book(**response.json).id == book_id


@pytest.mark.parametrize("book_id", [5])
def test_book_delete(setup, book_id):
    """Delete book with id 5"""
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    response = test_client.delete(__BASE_URL_ID.format(api_version, book_id))
    assert response.status_code == 204


@pytest.mark.parametrize("book_id", [3])
def test_bookitems_update_book_id_3_success(setup, book_id):
    """Receive one book has id 3"""
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    book_update = VALID_BOOK

    response = test_client.put(
        __BASE_URL_ID.format(api_version, book_id), json=book_update
    )

    assert response.status_code == 204


@pytest.mark.parametrize("book_id", [3])
def test_bookitems_patch_book_id_3_success(setup, book_id):
    """patch number of pages for book has id 3"""
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()
    book_patch = {"number_of_pages": 200}

    response = test_client.patch(
        __BASE_URL_ID.format(api_version, book_id), json=book_patch
    )

    assert response.status_code == 204


def test_book_create_book_title_book34_success(setup):
    """create a book has title book34"""
    api_version = setup.config.get("BLUEPRINTS").get("version")
    test_client = setup.test_client()

    response = test_client.post(__BASE_URL.format(api_version), json=VALID_BOOK)

    assert response.status_code == 201

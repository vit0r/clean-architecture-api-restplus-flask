"""Book API definitions"""

import re
from pathlib import Path

from app.v1 import Namespace, Resource
from app.v1.adapters import BookAdapter, BookSchema
from core.utils import get_namespace_model

__NAMESPACE = re.search(r".*(?=_api)", Path(__file__).stem, flags=re.IGNORECASE).group(
    0
)
NS_BOOK = Namespace(name=__NAMESPACE, description=__name__)

BOOK_API_MODEL = get_namespace_model("Book", NS_BOOK, BookSchema)


def abort_if_book_doesnt_exist(result):
    """Abort process with code 404 if not exists results"""
    if not result:
        NS_BOOK.abort(404, "Book not found")


def abort_if_book_crud_ops_fail(result):
    """Abort if process crud cause 500"""
    if not result:
        NS_BOOK.abort(500, "Crud OP's fail")


@NS_BOOK.route("/<int:book_id>")
@NS_BOOK.doc(responses={404: "Book not found"}, params={"book_id": "The Book ID"})
class Book(Resource):
    """Show a single book item and lets you delete them"""

    @classmethod
    @NS_BOOK.response(code=200, description="All books", model=BOOK_API_MODEL)
    def get(cls, book_id):
        """Fetch a given resource"""
        result = BookAdapter().find_by_id(book_id)
        abort_if_book_doesnt_exist(result)
        return result, 200

    @classmethod
    @NS_BOOK.response(code=204, description="Deleted book", model=BOOK_API_MODEL)
    def delete(cls, book_id):
        """Delete a given resource"""
        result = BookAdapter().delete(book_id)
        abort_if_book_crud_ops_fail(result)
        return "", 204

    @classmethod
    @NS_BOOK.response(code=204, description="book updated", model=BOOK_API_MODEL)
    def put(cls, book_id):
        """Update a given resource"""
        result = BookAdapter().update_or_patch(book_id, NS_BOOK.payload)
        abort_if_book_crud_ops_fail(result)
        return "", 204

    @classmethod
    @NS_BOOK.response(code=204, description="book patched", model=BOOK_API_MODEL)
    def patch(cls, book_id):
        """Patch a given resource"""
        result = BookAdapter().update_or_patch(book_id, NS_BOOK.payload)
        abort_if_book_crud_ops_fail(result)
        return "", 204


@NS_BOOK.route("/")
class BookItems(Resource):
    """all BOOKS, and lets you POST to add new book"""

    @classmethod
    @NS_BOOK.response(code=200, description="books list", model=BOOK_API_MODEL)
    def get(cls):
        """List all BOOKS"""
        result = BookAdapter().find_all()
        abort_if_book_doesnt_exist(result)
        return result, 200

    @classmethod
    @NS_BOOK.response(code=200, description="book created", model=BOOK_API_MODEL)
    @NS_BOOK.expect(BOOK_API_MODEL)
    def post(cls):
        """Create a book"""
        result = BookAdapter().create(NS_BOOK.payload)
        abort_if_book_crud_ops_fail(result)
        return "", 201

""" This Module contains the Unit Tests of the Book Repository"""
from core.repository.base_repository import BaseRepository
from core.repository.book_repository import BookRepository
from tests.mocked_books_formated import valid_book_list

# The following test is an Anti-Pattern.

# There are three reasons we shouldn't develop unit tests for our repository class.

# 1: Our repository only contain trivial code.
# 2: The following code is merely testing its own mocked Data; i.e. verifying if True == True
# 3: It's advisable to test all necessary integration with third party software.
#    Unless the code contain complex logic near its borders, which is a anti-pattern by itself,
#    unit testing a repository will test cases that must be tested in integration tests anyway.
#    The Developer should always try to write as few test as possible while still
#    guaranteeing the software's quality. This is the aim of the test pyramid.
#
# Still, this very basic test is a good example of how to mock another method in Python


def test_book_repository_find_all_success(mocker):
    """Should return all mocked books """

    # Arrange - Here is where you prepare your test. Gherkin equivalent is "Given"

    # Here is how you mock using
    mocker.patch("core.repository.base_repository.BaseRepository.find_all")
    result_mock = valid_book_list()
    BaseRepository.find_all.return_value = result_mock

    # Act - Here is where you make the testing action. Gherkin equivalent is "When"
    all_books = BookRepository().find_all()

    # Assert - Here is where verify the outcome of your test. Gherkin equivalent is "Then"
    assert all_books == result_mock

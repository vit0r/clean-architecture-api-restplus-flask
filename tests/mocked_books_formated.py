""" This module contains the methods that return the book objects used in the automated tests"""

from datetime import date

from core.entities import Book


def valid_book_list():
    """Returns a Valid Book List"""
    return [
        Book(
            id=1,
            title='Iracema',
            publication_date=date(1865, 3, 18),
            publisher='Typ. de Viana & Filhos',
            language='ptbr',
            number_of_pages=202,
            author='Jose de Alencar',
            synopsis='A Native American Priestess fall in love with an European and causes a war.'),
        Book(
            id=2,
            title='The Hobbit',
            publication_date=date(1937, 8, 29),
            publisher='Allen & Unwin',
            language='en',
            number_of_pages=389,
            author='J.R.R. Tolkien',
            synopsis=("A Hobbit goes on an adventure and finds something that"
                      " oughtn't to be found.")),
        Book(
            id=3,
            title='A Game of Thrones',
            publication_date=date(1996, 8, 1),
            publisher='Bantam Spectra',
            language='Common Tongue',
            number_of_pages=694,
            author='George R. R. Martin',
            synopsis='Everybody Dies.'),
        Book(
            id=4,
            title='Os Lusíadas',
            publication_date=date(1572, 8, 28),
            publisher='No Publisher',
            language='pt-pt',
            number_of_pages=559,
            author='Luís Vaz de Camões',
            synopsis="""Bold explorers ignore the ramblings of an old man and set forth in
                        a very long journey."""),
        Book(
            id=5,
            title='War and Peace',
            publication_date=date(1869, 3, 18),
            publisher='The Russian Messenger',
            language='ru',
            number_of_pages=1225,
            author='Leo Tolstoy',
            synopsis="""A Russian Bastard gets cheated by his wive and decides its his destiny
                        to kill Napoleon."""),
        Book(
            id=6,
            title='The Wealth of Nations',
            publication_date=date(1776, 8, 28),
            publisher='W. Strahan and T. Cadell',
            language='en',
            number_of_pages=950,
            author='Adam Smith',
            synopsis='A Scottish Philosopher discuss the powers of invisible hands.'),
        Book(
            id=7,
            title='The Prince',
            publication_date=date(1532, 8, 28),
            publisher="Antonio Blado d'Asola.",
            language='it',
            number_of_pages=136,
            author='Niccolò Machiavelli',
            synopsis=('A bitter Italian Diplomat makes a veiled attack on tyranny while explaining'
                      'how to be a proper tyrant.'))
    ]


def valid_book():
    """Returns a Valid Book"""
    return Book(
        title='Mistborn: The Final Empire',
        publication_date=date(2006, 7, 18),
        publisher='Tor Books',
        language='en',
        number_of_pages=541,
        author='Brandon Sanderson',
        synopsis=('A half-ska mistborn with trust issues joins a gang of thieves and set out to'
                  'destroy the tyrant that has been safeguarding humanity for a thousand years.'))


def invalid_title_book():
    """Returns a book with invalid Title"""
    return dict(
        title='',
        publication_date=date(2018, 8, 28),
        publisher='PUB',
        language='pt-br',
        number_of_pages=-2110,
        author='Author',
        synopsis='PUB1')


def invalid_id_book():
    """Returns a book with invalid id"""
    return Book(
        id=-200,
        title='Invalid ID Book',
        publication_date=date(2018, 8, 28),
        publisher='Random',
        language='binary',
        number_of_pages=1,
        author=("Someone who doesn't understand the importance of"
                "using  natural numbers in indexing"),
        synopsis="This book's purpose is too validate invalid data handling")


def valid_updated_book():
    """Returns a Valid Update for Book Example 3"""
    return Book(
        id=3,
        title='A Storm of Swords',
        publication_date=date(2000, 8, 8),
        publisher='Bantam Spectra',
        language='Common Tongue',
        number_of_pages=973,
        author='George R. R. Martin',
        synopsis="Everybody without plot armor dies.")


def incomplete_book():
    """Return a incomplete book"""
    return Book(
        title='Missing',
        publisher='',
        number_of_pages=973,
        synopsis="This book has several missing parameters")


def patched_title():
    """Return a Valid Title for update"""
    return 'Test update id 3'

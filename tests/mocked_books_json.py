"""This module contain the mock data used in the automated tests"""

VALID_BOOK_LIST = [
    {
        "title": "Iracema",
        "publication_date": "1865-03-18",
        "publisher": "Typ. de Viana & Filhos",
        "language": "ptbr",
        "number_of_pages": 202,
        "author": "Jose de Alencar",
        "synopsis": "A Native American Priestess fall in love with an European and causes a war.",
    },
    {
        "title": "The Hobbit",
        "publication_date": "1937-08-29",
        "publisher": "Allen & Unwin",
        "language": "en",
        "number_of_pages": 389,
        "author": "J.R.R. Tolkien",
        "synopsis": "A Hobbit goes on an adventure and finds something that oughtn't to be found.",
    },
    {
        "title": "A Game of Thrones",
        "publication_date": "1996-08-01",
        "publisher": "Bantam Spectra",
        "language": "Common Tongue",
        "number_of_pages": 694,
        "author": "George R. R. Martin",
        "synopsis": "Everybody Dies.",
    },
    {
        "title": "Os Lusíadas",
        "publication_date": "1572-08-28",
        "publisher": "No Publisher",
        "language": "pt-pt",
        "number_of_pages": 559,
        "author": "Luís Vaz de Camões",
        "synopsis": """Bold explorers ignore the ramblings of an old man and set forth in
                        a very long journey.""",
    },
    {
        "title": "War and Peace",
        "publication_date": "1869-3-18",
        "publisher": "The Russian Messenger",
        "language": "ru",
        "number_of_pages": 1225,
        "author": "Leo Tolstoy",
        "synopsis": """A Russian Bastard gets cheated by his wive and decides its his destiny
                        to kill Napoleon.""",
    },
    {
        "title": "The Wealth of Nations",
        "publication_date": "1776-08-28",
        "publisher": "W. Strahan and T. Cadell",
        "language": "en",
        "number_of_pages": 950,
        "author": "Adam Smith",
        "synopsis": "A Scottish Philosopher discuss the powers of invisible hands.",
    },
    {
        "title": "The Prince",
        "publication_date": "1532-08-28",
        "publisher": "Antonio Blado d'Asola",
        "language": "it",
        "number_of_pages": 136,
        "author": "Niccolò Machiavelli",
        "synopsis": """A bitter Italian Diplomat makes a veiled attack on tyranny while explaining
                        how to be a proper tyrant.""",
    },
]

VALID_BOOK = {
    "id": None,
    "title": "Mistborn: The Final Empire",
    "publication_date": "2006-07-18",
    "publisher": "Tor Books",
    "language": "en",
    "number_of_pages": 541,
    "author": "Brandon Sanderson",
    "synopsis": (
        "A half-ska mistborn with trust issues joins a gang of thieves and set out to"
        "destroy the tyrant that has been safeguarding humanity for a thousand years."
    ),
}

INCOMPLETE_BOOK = {
    "id": None,
    "title": "Misttorn: The FAKE Empire",
    "publication_date": "3236-12-27",
    "synopsis": "Move Along; nothing to see here",
}

INVALID_UPDATE_DATA = {"justABunchOf": "nonsense", "this": "json", "is": "invalid"}

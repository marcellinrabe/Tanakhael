"""Service around getting verse"""

import requests

# on development
PROXY = "http://localhost:8000"


def get(request):
    """the request function return the uri to fetch books from api"""

    def _build_url(uri):
        return f"{PROXY}/{uri}"

    def fetcher(*args, **kwargs):
        uri, params = request(*args, **kwargs)
        url = _build_url(uri)
        response = requests.get(
            url,
            {} if params is None else params
        )
        if response.status_code == 200:
            data = response.json()
            return data
        return None

    return fetcher


class VerseAPI:

    @get
    def testaments(self):
        """return bible Testaments"""
        return "testaments", {}

    @get
    def books(self, testament):
        """search all books of a given bible Testament name

        return list of books
        """
        testament_req = "_".join(
            testament.split(" ")
        )
        return "testament/books", {"testament": testament_req}

    @get
    def verse(self, testament, request_format):
        """request bible verse from api according to the request format

        Arguments:
        request_format str -- (example : Genesisy 1 : 2 - 3)

        return one object verse with information such as verse's book name, chapter, the text and verse number interval
        """

        return f"verse/{request_format}", {"testament": testament}

    @get
    def verse_number(self, book, chapter):
        testament_req = "_".join(
            book.testament.split(" ")
        )

        return "verse/count", {
            "testament": testament_req,
            "book": book.name,
            "chapter": chapter
        }

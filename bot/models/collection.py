"""collections model"""

from typing import List

from .book import Book


class Collection:

    def __init__(self, database, name):
        self.api_service = database.api_service
        self.name = name

    def get_books(self) -> List[Book]:
        params = {"collection": self.name}
        return self.api_service.get("collection/books", params)

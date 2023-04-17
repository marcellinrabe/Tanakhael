from services.verseapi import VerseAPI

# work when dev mode
PROXY = "http://localhost:8000/"


class Database:

    def __init__(self):
        self.api_service = VerseAPI(PROXY)
        self.collections = self._get_collections()

    def _get_collections(self):
        return self.api_service.get('collection/list')

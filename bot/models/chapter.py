

class Chapter:

    def __init__(self, book, index):
        self.book = book
        self.collection = self.book.collection
        self.index = index
        self.api_service = self.book.api_service
        self.verse_count = self._count_verse()

    def _count_verse(self):
        params = {
            "collection": self.collection.name,
            "book": self.book.name,
            "index": self.index
        }
        return self.api_service.get("chapter/verse/count", params)

    def get_verse(self, interval):
        verse = f"{self.book.name} {self.index} : {interval}"
        params = {"collection": self.collection.name}
        result = self.api_service.get(f"verse/{verse}", params)
        return {
            "book": result["book"],
            "chapter": result["chapter"],
            "pointer": result["pointer"],
            "end_cursor": result["end_cursor"],
            "verses": result["verses"]
        }

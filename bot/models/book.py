class Book:

    def __init__(self, collection, name):
        self.collection = collection
        self.name = name
        self.api_service = self.collection.api_service
        self.chapters_count = self._count_chapters()

    def _count_chapters(self):
        params = {
            "collection": self.collection.name,
            "book": self.name
        }
        return self.api_service.get("book/chapter/count", params)

    def __str__(self):
        return f"{self.name}"

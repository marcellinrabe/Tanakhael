"""Verse model"""

from re import match, sub


class Verse:

    def __init__(self, book, chapter, verse_interval):
        self.chapter = chapter
        self.book = self.add_space_between_book(book)
        self.pointer = self.find_pointer(verse_interval)
        self.limit = self.get_verse_limit(verse_interval)

    def add_space_between_book(self, book_name):
        pattern = r'(\d)([A-Z])'
        if match(pattern, book_name):
            return sub(pattern, r'\1 \2', book_name)
        return book_name

    def find_pointer(self, verse_interval):
        if "-" in verse_interval:
            begin, _ = verse_interval.split("-")
            return int(begin)

        return int(verse_interval)

    def get_verse_limit(self, verse_interval):
        if "-" in verse_interval:
            begin, end = verse_interval.split("-")
            begin, end = int(begin), int(end)
            if end < begin:
                return None
            return end - begin
        return 0



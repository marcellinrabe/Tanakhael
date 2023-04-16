"""All actions around uri"""

from re import match, findall

from .verse import Verse


class Uri:

    def __init__(self, string):
        self.string = string
        self.concatenate = self._concatenate()

    def _concatenate(self):
        """concatenate string without any whitespace"""
        if not isinstance(self.string, str):
            return None
        return self.string.replace(" ", "")

    def is_conform(self) -> bool:
        """verify if uri syntax match as app system required

        @return bool
        """
        pattern = r'^\d?[A-Z][a-z]{3,}\d{1,2}:\d{1,3}(-\d{1,2})?'
        is_conform = bool(match(pattern, str(self.concatenate)))
        return True if is_conform else False

    def parse_verse(self):

        pattern = r'\d?[A-Z][a-z]{3,}(\d+)?:'
        chapter_as_list = findall(pattern, self.concatenate)
        chapter = int(''.join(chapter_as_list))

        book, verse_interval = self.concatenate.split(f"{chapter}:")

        return book, chapter, verse_interval

    def build_filter(self):
        if not self.is_conform():
            return None

        book, chapter, verse_interval = self.parse_verse()
        verse = Verse(book, chapter, verse_interval)

        print(verse.limit)

        if verse.limit == 1:
            return {
                "arg_1": {
                    "meta.name": verse.book
                },
                "arg_2": {
                    f"{verse.chapter}": {
                        f"{verse.pointer}": 1
                    },
                    "_id": 0
                }
            }

        elif verse.limit > 1:
            arg_2 = {f"{i}": 1 for i in range(verse.pointer, verse.pointer + verse.limit + 1)}

            return {
                "arg_1": {
                    "meta.name": verse.book
                },
                "arg_2": {
                    f"{verse.chapter}": arg_2,
                    "_id": 0
                },
            }

class Book:

    def __init__(self, testament, name, chapter_number):
        self.testament = testament
        self.name = name
        self.chapter_number = chapter_number

    def __str__(self):
        return f"{self.name}"

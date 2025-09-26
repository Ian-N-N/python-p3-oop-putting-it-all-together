#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # title property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            print("Title must be a non-empty string.")
            self._title = "Unknown"
        else:
            self._title = value.strip()

    # page_count property
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = 0
        elif value <= 0:
            print("page_count must be a positive integer")
            self._page_count = 0
        else:
            self._page_count = value

    # ✅ NEW METHOD to pass test
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"'{self.title}' with {self.page_count} pages"

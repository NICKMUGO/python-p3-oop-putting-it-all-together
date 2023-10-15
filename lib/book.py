class Book:
    def __init__(self,title,page_count):
        self._page_count=page_count
        self.page_count=page_count
        self.title=title
    def get_page(self):
        return self._page_count
    def set_page(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    page_count=property(get_page, set_page)
book = Book("And Then There Were None", 272)
print(book.page_count)
print(book.title)

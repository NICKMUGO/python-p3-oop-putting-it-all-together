class Book:
    def __init__(self,title,page_count):
        self.page_count=page_count
        self.title=title
    def page_count(self):
        return self._page_count
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
book = Book("And Then There Were None", 272)
print(book.page_count)
print(book.title)

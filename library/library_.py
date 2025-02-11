from library.book import Book

class Library:
    def __init__(self, storage):
        self.books = {}
        self.storage = storage
        self.last_id = None

    def _get_last_id_book(self):
        last_id = self.storage.get_last_id()
        return last_id

    def increment_book_id(self):
        self.last_id = int(self._get_last_id_book())
        self.last_id += 1
        self.storage.increment_last_id()

    def add_book(self, book):
        if isinstance(book, Book):
            self.increment_book_id()
            book.id = str(self.last_id)
            self.storage.write_data(book.to_dict())
            return book
        raise ValueError("Неверный формат книги!")

    # def get_book_info(self, book_id):
    #     return self.books.get(book_id)

    def get_book_by_id(self, book_id):
        book = self.books.get(book_id)
        if book:
            return book
        raise ValueError("Такой книги нет")

    def get_book_by_isbn(self, isbn):
        for id_, book in self.books.items():
            if isbn == book.get("isbn"):
                return id_, book
        raise ValueError("Такой книги нет")

    def get_books(self):
        books = self.storage.read_data()
        books_obj = []
        for book in books:

        return self.books

    def get_books_by_author(self, author):
        books = {}
        for id_, book in self.books.items():
            if author.lower() in book.author.lower():
                books[id_] = book
        return books

    def get_books_by_title(self, title):
        books = {}
        for id_, book in self.books.items():
            if title.lower() in book.title.lower():
                books[id_] = book
        return books

    def search_book(self, query):
        results = {}
        for id_, book in self.books.items():
            if query.lower() in book.author.lower():
                results[id_] = book
        return results

    def book_delete(self, id_):
        if id_.isdigit():
            if int(id_) in self.books:
                return self.books.pop(int(id_))
            else:
                raise ValueError("Неверный или некорректный id")

    # @classmethod
    # def get_book_count(cls):
    #     return cls.id_
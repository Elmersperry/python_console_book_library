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

    def get_book_by_id(self, book_id):
        book = self.books.get(book_id)
        if book:
            return book
        raise ValueError("Такой книги нет")

    def get_book_by_isbn(self, isbn):
        results = []
        books = self.storage.read_data()
        for item in books:
            if isbn.lower() in item["ISBN"].lower():
                results.append(Book.from_dict(item))
        return results
        # for id_, book in self.books.items():
        #     if isbn == book.get("isbn"):
        #         return id_, book
        # raise ValueError("Такой книги нет")

    def get_books(self):
        books = self.storage.read_data()
        books_obj = []
        for book in books:
            books_obj.append(book)
        return books_obj

    def get_books_by_request(self, request):
        results = []
        books = self.storage.read_data()
        for item in books:
                if request.lower() in item["author"].lower() or item["title"].lower or item["ISBN"].lower():
                    results.append(Book.from_dict(item))
        return results

    def get_books_by_author(self, author):
        results = []
        books = self.storage.read_data()
        for item in books:
                if author.lower() in item["author"].lower():
                    results.append(Book.from_dict(item))
        return results

    def get_books_by_title(self, title):
        results = []
        books = self.storage.read_data()
        for item in books:
            if title.lower() in item["title"].lower():
                results.append(Book.from_dict(item))
        return results

    def search_book(self, query):
        results = {}
        for id_, book in self.books.items():
            if query.lower() in book.author.lower():
                results[id_] = book
        return results

    def book_delete(self, isbn: str):
        books = self.storage.read_data()
        for i, book in enumerate(books):
            if book["isbn"].lower() == isbn.lower():
                books.pop(i)

        self.storage.file.seek(33)
        self.storage.file.truncate()

        for book in books:
            self.add_book(Book.from_dict(book))

        # if id_.isdigit():
        #     if int(id_) in self.books:
        #         return self.books.pop(int(id_))
        #     else:
        #         raise ValueError("Неверный или некорректный id")
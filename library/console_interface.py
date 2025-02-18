import sys
from library import Book

class ConsoleInterface:
    def __init__(self, source):
        self.library = source

    def main_menu(self):
        print("Добро пожаловать в ИС 'Электронная библиотека'")
        print("Выберите нужное действие:")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Поиск книг")
        print("4. Удалить книгу")
        print("0. Выйти")

        self.process_main_menu()

    def process_main_menu(self):
        action = input(">>> ")
        match action:
            case "1":
                self.show_books()
            case "2":
                self.add_book()
            case "3":
                self.search_book()
            case "4":
                self.delete_book()
            case "0":
                sys.exit()
            case _:
                print("Выберите нужный пункт меню!")

    @staticmethod
    def show_books_info(books):
        for book in books:
            print(book.get_info())

    def show_books(self):
        books = self.library.get_books()
        self.show_books_info(books)
        self.footer_menu()

    def add_book(self):
        author = input("Введите автора: ")
        title = input("Введите название: ")
        year = input("Введите год: ")
        genre = input("Введите жанр: ")
        try:
            book = Book(author=author,
                        title=title,
                        year=year,
                        genre=genre)
            self.library.add_book(book)
            print("Книга успешно добавлена!")
        except ValueError as err:
            print(err)
            self.add_book()
        self.footer_menu()

    def search_book(self):
        print("Поиск книги")
        self.process_search_book()
        self.footer_menu()

    def process_search_book(self):
        text = ("31. Поиск по автору\n"
                "32. Поиск по названию\n"
                "33. Поиск по ISBN")
        print(text)
        print("Введите 1 для выхода в главное меню")
        print("Введите 0 для выхода из программы")
        new_action = input(">>> ")
        match new_action:
            case "31":
                author = input("Введите автора: ")
                books = self.library.get_books_by_author(author)
                if books:
                    self.show_books_info(books)
                else:
                    print("По вашему запросу книг не найдено")
            case "32":
                title = input("Введите название: ")
                books = self.library.get_books_by_title(title)
                if books:
                    self.show_books_info(books)
                else:
                    print("По вашему запросу книг не найдено")
            case "33":
                isbn = input("Введите название: ")
                books = self.library.get_books_by_title(isbn)
                if books:
                    self.show_books_info(books)
                else:
                    print("По вашему запросу книг не найдено")
            case "1":
                self.main_menu()
            case "0":
                sys.exit()
            case _:
                print("Выберите нужный пункт")
                self.process_search_book()

    def delete_book(self):
        isbn = print("Введите ISBN книги для удаления: ")
        if self.library.check_book(isbn):
            self.library.book_delete(isbn)
        else:
            print("Такой книги нет!")
        self.footer_menu()

    def footer_menu(self):
        print("Введите 1 для выхода в главное меню")
        print("Введите 0 для выхода из программы")
        action = input(">>> ")
        match action:
            case "1":
                self.main_menu()
            case "0":
                sys.exit()
            case _:
                print("Выберите необходимое действие")
                self.footer_menu()

    def check_book(self, isbn):
        books = self.library.read_data()
        for item in books:
            if item["ISBN"].lower() == isbn.lower():
                return item["ISBN"]
        return None
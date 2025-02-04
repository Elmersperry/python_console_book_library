class ConsoleInterface:
    @staticmethod
    def main_menu():
        print("Добро пожаловать в ИС 'Электронная библиотека'")
        print("Выберите нужное действие:")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Поиск книг")
        print("4. Удалить книгу")
        print("0. Выйти")

    @staticmethod
    def process_main_menu():
        action = input(">>> ")
        print(action)

    @staticmethod
    def show_books(books):
        for id_, book in books.items():
            print(f"{id_}.{book.get_info()}")

    @staticmethod
    def add_book():
        author = input("Введите автора: ")
        title = input("Введите название: ")
        year = input("Введите год: ")
        genre = input("Введите жанр: ")
        return {
            "author": author,
            "title": title,
            "year": year,
            "genre": genre
        }

    @staticmethod
    def search_book():
        pass

    @staticmethod
    def delete_book():
        pass

    @staticmethod
    def exit():
        pass
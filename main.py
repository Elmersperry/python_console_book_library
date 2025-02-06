from library import Book, Library, ConsoleInterface
from db import CSVStorage

def main():
    csv_storage = CSVStorage("books.csv")
    library = Library(storage=csv_storage)
    console = ConsoleInterface(source=library)

    while True:
        console.main_menu()

    # book_1 = Book(title="Капитанская дочка", author="А. С. Пушкин", year=1836, genre="Роман")
    # book_2 = Book(title="Герой нашего времени", author="М. Ю. Лермонтов", year=1836, genre="Роман")
    # library.add_book(book_1)
    # library.add_book(book_2)
    # books = library.get_books()
    # for id_, book in books.items():
    #     print(book.get_info())
    #
    # print(Library.get_book_count())
    #
    # query = "пуш"
    # results = library.search_book(query)
    # if results:
    #     print("Найденные книги:")
    #     for id_, book in results.items():
    #         print(book.get_info())
    # else:
    #     print("Ничего не найдено")
    #
    # id_for_del = "2"
    # book_deleted = library.book_delete(id_for_del)
    # print(f"Удалённая книга - {book_deleted.get_info()}")
    # books = library.get_books()
    # for id_, book in books.items():
    #     print(book.get_info())

if __name__ == "__main__":
    main()
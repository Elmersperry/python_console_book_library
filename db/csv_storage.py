import csv
import os


class CSVStorage:
    def __init__(self, filename):
        file_exist = os.path.isfile(filename)
        self.file = open(filename, mode="a+", encoding="utf-8")
        fields = ["author", "title", "year", "genre", "ISBN"]
        writer = csv.DictWriter(self.file, fieldnames=fields)
        if not file_exist:
            writer.writeheader()

    def write_data(self, book):
        writer = csv.DictWriter(self.file, fieldnames=book.keys())
        writer.writerow(book)
        # self.file.close()

    def read_data(self):
        pass
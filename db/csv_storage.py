import csv
import os

class CSVStorage:
    def __init__(self, filename):
        self.filename = filename
        file_exist = os.path.isfile(filename)
        if file_exist:
            self.last_id = self.get_last_id()
        else:
            self.last_id = "0"

        self.file = open(filename, "a+", encoding="utf-8")
        fields = ["id", "author", "title", "year", "genre", "ISBN"]
        writer = csv.DictWriter(self.file, fieldnames=fields)
        if not file_exist:
            writer.writeheader()

    def get_last_id(self):
        self.file = open(self.filename, "a+", encoding="utf-8")
        data = self.read_data()
        if data:
            last_id = data[-1].get("id")
            return last_id
        else:
            return "0"

    def write_data(self, book: dict):
        writer = csv.DictWriter(self.file, fieldnames=book.keys())
        writer.writerow(book)

    def increment_last_id(self):
        self.last_id = str(int(self.last_id) + 1)

    def read_data(self):
        self.file.seek(0)
        reader = csv.DictReader(self.file)
        return list(reader)
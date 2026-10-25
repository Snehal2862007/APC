# import re

# dictionary = {"python", "java", "program", "computer", "student", "hello", "world", "is", "a", "language"}

# text = input("enter text: ").lower()

# words = re.findall(r"\b[a-z]+\b", text)

# wrong = []

# for word in words:
#     if word not in dictionary and word not in wrong:
#         wrong.append(word)

# print("misspelled words:", wrong)




class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "available"

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
        else:
            print("book already borrowed")

    def return_book(self):
        self.status = "available"

    def display(self):
        print("title:", self.title)
        print("author:", self.author)
        print("year:", self.year)
        print("status:", self.status)

b = Book("python", "guido", 2020)

b.display()
b.borrow()
b.display()
b.return_book()
b.display()
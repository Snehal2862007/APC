books = {}

def add_book(name):
    books[name] = True

def issue_book(name):
    if books.get(name):
        books[name] = False
        return "issued"
    return "not available"

def return_book(name):
    if name in books:
        books[name] = True
        return "returned"
    return "book not found"

def search_book(name):
    return books.get(name, "not found")

def display_books():
    return [b for b in books if books[b]]

add_book("python")
add_book("java")
print(issue_book("python"))
print(search_book("python"))
print(return_book("python"))
print(display_books())
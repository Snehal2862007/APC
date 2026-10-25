import csv
from pathlib import Path
file = Path("books.csv")
def load():
    if not file.exists():
        return []
    with file.open(newline="") as f:
        return list(csv.DictReader(f))
def save(books):
    with file.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "author", "available"])
        w.writeheader()
        w.writerows(books)
books = load()
while True:
    print("1 add  2 search  3 issue  4 return  5 available  0 exit")
    choice = input("choice: ")
    if choice == "0":
        break
    if choice == "1":
        bid = input("id: ")
        if any(b["id"] == bid for b in books):
            print("id already exists")
        else:
            books.append({"id": bid, "title": input("title: "), "author": input("author: "), "available": "yes"})
    elif choice in ("2", "3", "4"):
        bid = input("book id: ")
        book = next((b for b in books if b["id"] == bid), None)
        if not book:
            print("not found")
        elif choice == "2":
            print(book)
        elif choice == "3" and book["available"] == "yes":
            book["available"] = "no"
            print("issued")
        elif choice == "4" and book["available"] == "no":
            book["available"] = "yes"
            print("returned")
        else:
            print("operation unavailable")
    elif choice == "5":
        for b in books:
            if b["available"] == "yes":
                print(b)
    save(books)

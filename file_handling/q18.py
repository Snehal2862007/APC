import csv
rows = [[1, "amit", "it", 40000], [2, "priya", "hr", 50000], [3, "rahul", "sales", 35000]]
with open("employees.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "name", "department", "salary"])
    w.writerows(rows)
with open("employees.csv", newline="") as f:
    employees = list(csv.DictReader(f))
def display():
    for e in employees:
        print(e)
def highest():
    print(max(employees, key=lambda e: float(e["salary"])))
def average():
    print(sum(float(e["salary"]) for e in employees) / len(employees))
def above(amount):
    for e in employees:
        if float(e["salary"]) > amount:
            print(e)
display()
highest()
average()
above(float(input("minimum salary: ")))

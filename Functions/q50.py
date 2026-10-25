employees = [
    ("ram", "it", 40000),
    ("sita", "hr", 60000),
    ("shyam", "sales", 55000)
]

high = list(filter(lambda x: x[2] > 50000, employees))
increased = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))
ordered = sorted(employees, key=lambda x: x[2])

print("high salary:", high)
print("increased salary:", increased)
print("sorted:", ordered)
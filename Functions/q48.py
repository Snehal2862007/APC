employees = [("ram", 30000), ("sita", 50000), ("shyam", 40000)]
result = sorted(employees, key=lambda x: x[1])
print(result)
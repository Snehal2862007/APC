import re
files = input("enter filenames separated by space: ").split()
count = {}
for file in files:
    match = re.search(r'\.[a-zA-Z0-9]+$', file)
    if match:
        ext = match.group()
        count[ext] = count.get(ext, 0) + 1
print(count)
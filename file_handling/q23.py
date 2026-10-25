from itertools import zip_longest
with open("first.txt") as a, open("second.txt") as b:
    for n, (x, y) in enumerate(zip_longest(a, b), 1):
        if x != y:
            print("different at line", n)
            break
    else:
        print("identical")

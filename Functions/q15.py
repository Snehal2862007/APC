def unique(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

print(unique([1, 2, 2, 3, 3]))
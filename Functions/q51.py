products = [
    ("pen", 20, 10),
    ("book", 200, 8),
    ("bag", 1500, 2)
]

def total(p):
    return p[1] * p[2]

values = list(map(lambda x: (x[0], total(x)), products))
costly = list(filter(lambda x: x[1] > 1000, products))
ordered = sorted(products, key=lambda x: total(x))

print("total values:", values)
print("costly products:", costly)
print("sorted:", ordered)
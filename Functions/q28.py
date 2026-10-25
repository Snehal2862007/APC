cart = {}

def add_product(name, price, qty):
    cart[name] = [price, qty]

def remove_product(name):
    cart.pop(name, None)

def subtotal():
    return sum(p * q for p, q in cart.values())

def coupon(amount):
    return amount * 0.90

def gst(amount):
    return amount * 0.18

def invoice():
    amount = coupon(subtotal())
    return amount + gst(amount)

add_product("pen", 20, 5)
add_product("book", 100, 2)

print("subtotal:", subtotal())
print("final bill:", invoice())
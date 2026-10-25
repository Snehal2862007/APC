from products.pricing import price
def total(order): return price(order["product"])*order["quantity"]

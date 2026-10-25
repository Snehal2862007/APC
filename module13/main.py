from products.catalog import show
from customers.profile import name
from orders.create import create
from orders.total import total
from payments.method import method
from payments.receipt import receipt
show()
order=create(2,3)
print(name(),order,total(order),method(),receipt(total(order)))

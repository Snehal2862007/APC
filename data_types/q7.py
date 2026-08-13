inventory={}
def add_product(name,qty):
    inventory[name]=qty
    print("product added")
def update_product(name,qty):
    if name in inventory:
        inventory[name]=qty
        print("product updated")
        if inventory[name]==0:
            del inventory[name]
            print("product removed")
    else:
        print("product not found")
def highest_stock():
    if len(inventory)==0:
        print("inventory is empty")
    else:
        product=max(inventory,key=inventory.get)
        print("highest stock:",product,inventory[product])
def display():
    if len(inventory)==0:
        print("inventory is empty")
    else:
        for i in inventory:
            print(i,":",inventory[i])
def total_products():
    print("total unique products:",len(inventory))
while True:
    print("\n1.add product")
    print("2.update product")
    print("3.display highest stock")
    print("4.display inventory")
    print("5.total unique products")
    print("6.exit")
    choice=int(input("enter choice: "))
    if choice==1:
        name=input("enter product name: ")
        qty=int(input("enter quantity: "))
        add_product(name,qty)
    elif choice==2:
        name=input("enter product name: ")
        qty=int(input("enter new quantity: "))
        update_product(name,qty)
    elif choice==3:
        highest_stock()
    elif choice==4:
        display()
    elif choice==5:
        total_products()
    elif choice==6:
        print("exit")
        break
    else:
        print("invalid choice")
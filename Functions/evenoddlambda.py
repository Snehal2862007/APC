x=int(input("enter a number: " ))
print((lambda x: "even" if x % 2 == 0 else "odd")(x))
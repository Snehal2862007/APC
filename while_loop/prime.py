n = int(input("enter a number: "))
if n < 2:
    print("Not Prime")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")
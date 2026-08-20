arr=[]
n=int(input("enter the number of elements: "))
for i in range(n):
    arr.append(int(input("enter the element: ")))

target=int(input("enter the element to search: "))
for i in range(n):
    if arr[i]==target:
        print(target,"found at index:",i)
        break;
    if i==n-1:
        print(target,"not found")



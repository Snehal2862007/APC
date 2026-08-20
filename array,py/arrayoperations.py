n=int(input("enter the number of elements: "))
arr=[]

for i in range(n):
    arr.append(int(input("enter a numbers:")))
arr.append(5)
print(arr)
arr.insert(10,0)
print(arr)
arr.pop(5)
print(arr)
arr.remove(2)
print(arr)






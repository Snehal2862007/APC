r=int(input("enter the radius:"))
def area(r):
    if r==0:
        print("area =0")
    else:
        result=3.142*r**2
        print("area=",result)
area(r)
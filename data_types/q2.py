import math
def distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
def farthest(points):
    far=points[0]
    maxd=math.sqrt(far[0]**2+far[1]**2)
    for p in points:
        d=math.sqrt(p[0]**2+p[1]**2)
        if d>maxd:
            maxd=d
            far=p
    return far
points=[]
n=int(input("enter number of points: "))
for i in range(n):
    x=int(input("enter x: "))
    y=int(input("enter y: "))
    points.append((x,y))
print("Points:",points)
i1=int(input("enter first point index: "))
i2=int(input("enter second point index: "))
print("distance:",distance(points[i1],points[i2]))
print("farthest point:",farthest(points))
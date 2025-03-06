import math

points = {}
distance = {}
dist = 0

dimensions = int(input("Input number of dimensions:\n"))
for i in range(1,3):
    for j in range(1 ,(dimensions+1)):
        position = int(input("Input Point %s dimension %s value:\n" % (i,j)))
        points.update({"p"+ str(i) + str(j): position})
        if i == 2:
            distance.update({str(j): abs(points["p1" + str(j)]-points["p2" + str(j)])})

for i in range(1,(dimensions+1)):
    dist = dist + (distance[str(i)] * distance[str(i)])


dist = math.sqrt(dist)
print(dist)

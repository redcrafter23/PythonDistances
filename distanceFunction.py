import math
point1 = [1,123,23,-46]
point2 = [234,-346,6,89]
dimensions = 4
distances = []
resultDistance= 0


def ddistance(point1, point2, dimensions):
    for i in range(dimensions):
        distances.append(abs(point1[i] - point2[i]))
        resultDistance = resultDistance + distances[i]
    return resultDistance


ddistance(point1,point2,dimensions)
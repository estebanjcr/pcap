# points on a plane

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        __dist = math.hypot(self.getx(), self.gety())
        return __dist

    def distance_from_point(self, point):
        __dist = math.hypot(point.getx(), point.gety())
        return __dist

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

"""
X: horizontal
Y: vertical

   Y
   |
   |
------- X
   |
   |
"""
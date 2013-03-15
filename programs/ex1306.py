#!/usr/bin/env python

from math import sqrt, fabs

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)

    def __repr__(self):
        return repr(((self.start.x, self.start.y), (self.end.x, self.end.y)))

    __str__ = __repr__

    def length(self):
        return sqrt((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2)

    def slope(self):
        X = self.start.x - self.end.x
        Y = self.start.y - self.end.y
        if 0 == X:
            return None
        return fabs(Y / X)

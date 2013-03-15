#!/usr/bin/env python

class HideX(object):
    def __init__(self, x):
        self.__x = ~x

    def x():
        def fget(self):
            return ~self.__x

        def fset(self, x):
            assert isinstance(x, int), '"x" must be an integer!'
            self.__x = ~x

        return locals()

    x = property(x())


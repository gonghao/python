#!/usr/bin/env python

class Stack(list):
    def __init__(self, *args):
        super(self.__class__, self).__init__(args)

    def push(self, data):
        self.append(data)
    
    def isempty(self):
        return 1 if len(self) == 0 else 0

    def peek(self):
        return self[-1]

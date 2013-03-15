#!/usr/bin/env python

class Ex3(object):
    '图的m着色问题'
    def __init__(self, a, m):
        self.a = a
        self.n = len(a)
        self.x = [0 for i in range(self.n)]
        self.m = m
        self.sum = 0
    
    def mColoring(self):
        self.backtrack(0)
        return self.sum

    def backtrack(self, t):
        if t > self.n - 1:
            self.sum += 1
            for i in range(self.n):
                print '%d ' % self.x[i],
            print
        else:
            for i in range(1, self.m + 1):
                self.x[t] = i;
                if self.ok(t):
                    self.backtrack(t + 1)
                self.x[t] = 0

    def ok(self, k):
        for i in range(self.n):
            if self.a[k][i] and self.x[i] == self.x[k]:
                return False
        return True

def main():
    graph = [[0, 1, 1, 1, 0],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 1, 0],
             [1, 1, 1, 0, 1],
             [0, 1, 0, 1, 0]]
    exp = Ex3(graph, 4)
    m = exp.mColoring()
    print 'This graph has %d schemes to color' % m

if __name__ == '__main__':
    main()

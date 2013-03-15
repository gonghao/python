#!/usr/bin/env python

class Ex11(object):
    '动态规划算法'
    def __init__(self, p):
        self.p = p
        n = len(p)
        self.m = [[0 for col in range(n + 1)] for row in range(n + 1)]
        self.s = [[0 for col in range(n + 1)] for row in range(n + 1)]
        self._addCount = 0
        self._mulCount = 0
        self._cmpCount = 0

    def matrixChain(self):
        addCount = 0
        mulCount = 0
        cmpCount = 0
        m = self.m
        s = self.s
        p = self.p
        n = len(m)
        for r in range(1, n):
            for i in range(n - r - 1):
                j = i + r
                m[i][j] = m[i + 1][j] + p[i - 1] * p[i] * p[j]
                s[i][j] = i
                addCount += 1
                mulCount += 2
                for k in range(i + 1, j):
                    t = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                    addCount += 2
                    mulCount += 2
                    if t < m[i][j]:
                        m[i][j] = t
                        s[i][j] = k
        self._addCount = addCount
        self._mulCount = mulCount
        self._cmpCount = cmpCount

    def traceback(self, i, j):
        if i == j:
            return
        self.traceback(i, self.s[i][j])
        self.traceback(self.s[i][j] + 1, j)
        print 'Multipy A%d,%d and A%d,%d' % (i + 1, self.s[i][j] + 1, self.s[i][j] + 2, j + 1)

def main():
    p = [35, 15, 5, 10, 20, 25]
    exp = Ex11(p)
    n = len(p)
    exp.matrixChain()
    for i in range(n):
        for j in range(i, n):
            print 'm%d%d = %d\t' % (i, j, exp.m[i][j]),
        print
    for i in range(n):
        for j in range(i, n):
            print 's%d%d = %d\t' % (i, j, exp.s[i][j]),
        print
    exp.traceback(0, n - 1)

if __name__ == '__main__':
    main()

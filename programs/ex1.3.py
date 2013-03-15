#/usr/bin/env python

class Ex13(object):
    '备忘录算法'
    def __init__(self, p):
        self.p = p
        n = len(p)
        self.s = [[0 for col in range(n + 1)] for row in range(n + 1)]
        self.m = [[0 for col in range(n + 1)] for row in range(n + 1)]

    def lookupChain(self, i, j):
        p = self.p
        s = self.s
        m = self.m
        if m[i][j] > 0:
            return m[i][j]
        if i == j:
            return 0
        u = self.lookupChain(i + 1, j) + p[i - 1] * p[i] * p[j]
        s[i][j] = i
        for k in range(i + 1, j):
            t = self.lookupChain(i, k) + self.lookupChain(k + 1, j) + p[i - 1] * p[k] * p[j]
            if t < u:
                u = t
                s[i][j] = k
        m[i][j] = u
        return u

def main():
    p = [35, 15, 5, 10, 20, 25]
    exp = Ex13(p)
    n = len(p)
    exp.lookupChain(0, n - 1)
    for i in range(n):
        for j in range(n):
            print 's%d%d = %d\t' % (i, j, exp.s[i][j]),
        print

if __name__ == '__main__':
    main()

#/usr/bin/env python

class Ex12(object):
    'µ›πÈÀ„∑®'
    def __init__(self, p):
        self.p = p
        n = len(p)
        self.s = [[0 for col in range(n + 1)] for row in range(n + 1)]

    def recurMatrixChain(self, i, j):
        if i == j:
            return 0
        p = self.p
        s = self.s
        u = self.recurMatrixChain(i + 1, j) + p[i - 1] * p[i] * p[j]
        s[i][j] = i
        for k in range(i + 1, j):
            t = self.recurMatrixChain(i, k) + self.recurMatrixChain(k + 1, j) + p[i - 1] * p[k] * p[j]
            if t < u:
                u = t
                s[i][j] = k
        return u

def main():
    p = [35, 15, 5, 10, 20, 25]
    exp = Ex12(p)
    n = len(p)
    exp.recurMatrixChain(0, n - 1)
    for i in range(n):
        for j in range(n):
            print 's%d%d = %d\t' % (i, j, exp.s[i][j]),
        print

if __name__ == '__main__':
    main()

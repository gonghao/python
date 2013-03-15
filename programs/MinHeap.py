#!/usr/bin/env python

class MinHeap(object):
    '最小堆类'
    def __init__(self, q):
        n = len(q)
        for i in range(1, n + 1):
            self.heap[i] = q[i - 1]
        self.size = n

    def leftChild(self, pos):
        return pos * 2

    def rightChild(self, pos):
        return pos * 2 + 1

    def parent(self):
        return pos / 2

    def isLeaf(self, pos):
        return pos > size / 2 and pos <= size

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def insert(self, ele):
        self.size += 1
        heap = self.heap
        heap[self.size] = ele
        cur = self.size
        while heap[cur] < heap[self.parent(cur)]:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)

    def removeMin(self):
        self.swap(1, self.size)
        self.size -= 1
        if self.size:
            self.pushdown(1)
        return self.heap[self.size + 1]

    def pushdown(self, pos):
        heap = self.heap
        while not self.isLeaf(pos):
            smallest = self.leftChild(pos)
            if smallest < self.size and heap[smallest] > heap[smallest + 1]:
                smallest += 1
            if heap[pos] <= heap[smallest]:
                return
            self.swap(pos, smallest)
            pos = smallest

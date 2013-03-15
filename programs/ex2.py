#!/usr/bin/env python

from MinHeap import MinHeap
from Bintree import Bintree

class Huffman(object):
    '哈夫曼类'
    def __init__(self, t, w):
        self.tree = t
        self.weight = w

    def __cmp__(self, obj):
        return cmp(self.weight, obj.weight)

def huffmanTree(f):
    '通过一频率列表建立哈夫曼树'
    n = len(f)
    w = {}
    zero = Bintree()
    for i in range(n):
        x = Bintree()
        x.makeTree(i, zero, zero)
        w[i] = Huffman(x, f[i])

    H = MinHeap(w)

    for i in range(1, n):
        x = H.removeMin()
        y = H.removeMin()
        z = Bintree()
        z.makeTree(l = x.tree, r = y.tree)
        t = Huffman(z, x.weight + y.weight)
        H.insert(t)

    return H.removeMin().tree

def main():
    #TODO: 从txt文件读取所有字符，建立字符频率列表f
    ht = huffmanTree(f)
    #TODO: 从生成的哈夫曼树ht中建立加密字典表enconde
    #TODO: 利用加密字典表encode加密txt文件，生成加密后文件，encodeFile
    #TODO: 利用enchodeFile和加密字典表encode解密文件

if __name__ == '__main__':
    main()

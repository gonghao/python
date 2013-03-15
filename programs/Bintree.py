#!/usr/bin/env python

class Bintree(object):
    '二叉树类'
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def makeTree(self, data = None, l = None, r = None):
        self.data = data
        self.left = l
        self.right = r

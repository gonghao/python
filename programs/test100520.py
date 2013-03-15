#!/usr/bin/env python
# encoding=utf-8

def hello():
    print 'Hello World!'

def foo():
    hello()
    print 'This is foo'

if '__main__' == __name__:
    foo()

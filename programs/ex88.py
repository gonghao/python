#!/usr/bin/env python
#encoding=utf-8

def factorial(n):
    if n < 1:
        raise Exception, 'Input N must be greater than ZERO.'
    if 1 == n:
        return 1
    else:
        return n * factorial(n - 1)

#!/usr/bin/env python
#encoding=utf-8
def isPrime(num):
    u'判断素数'
    count = num / 2
    while count > 1:
        if 0 == num % count:
            return False
        count -= 1
    else:
        return True

def getFactors(num):
    u'获取指定数的所有约数'
    factors = []
    for i in range(1, num + 1):
        if 0 == num % i:
            factors.append(i)
    return factors

def primeFactorize(num):
    u'分解指定数的质因数'
    primeFactors = []
    if isPrime(num):
        primeFactors.append(num) 
    else:
        maxFactor = getFactors(num)[-2]
        primeFactors.append(num / maxFactor)
        primeFactors += primeFactorize(maxFactor)
    return primeFactors

def isPerfectNumber(num):
    u'判断给定数是否为完全数'
    factors = getFactors(num)[: -1]
    if sum(factors) == num:
        return 1
    return 0

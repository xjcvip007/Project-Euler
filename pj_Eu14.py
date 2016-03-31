# -*- code:utf-8 -*-
import math
a = {}
def chain_len(n):
    if n==1:
        return 1
    n = 3*n+1 if n&1 else n/2
    if n in a:
        l = a[n] + 1
    else:
        l = chain_len(n) + 1
    a[n] = l
    return l

max,max_i = 0,0
for i in xrange(1,1000000):
    l = chain_len(i)
    if l > max:
        max,max_i = l,i
print max_i

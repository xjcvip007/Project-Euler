# -*- code:utf-8 -*-
import math
cache = {(0, 0):1} #reduce dup computations

def F(n, m):
    if not n or not m:
        return 1
    if (n,m) in cache:
        return cache[(n,m)]
    local_sum = 0
    for i in range(0, n):
        local_sum += F(i, m-1)
    for i in range(0, m):
        local_sum += F(n-1, i)
    cache[(n,m)] = local_sum
    if n != m:
        cache[(m,n)] = local_sum
    return local_sum

i=20
print F(i, i)
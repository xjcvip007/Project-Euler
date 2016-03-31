import math
def factor_count(n):
    count = 0
    sq = int(math.sqrt(n))
    for i in xrange(1,sq+1):
        if n%i == 0:
            count += 2
    if sq * sq == n:
        count -= 1
    return count

i,n = 1,1
while True:
    i += 1
    n += i
    if n < 250 * 250: continue #the smallest
    if factor_count(n) > 500:
        print n
        break
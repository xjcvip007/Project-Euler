# -*- code:utf-8 -*-
import math
def add(x,y):
    return x+y
n100 = "hundred"
n1000 = "thousand"
single = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
n10 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
sum_9 = sum([len(i) for i in single[:10]])
sum_99 = 10*sum([len(i) for i in n10]) + 9*sum_9 + sum([len(i) for i in single[11:]]) + len(single[10])
sum_1000 = 100 * sum_9 + 900 * len(n100) + 10 * sum_99 + len(n1000) + len(single[1]) + 9*99*len("and")
print sum_1000

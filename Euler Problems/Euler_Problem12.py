#Euler Problem 12
import math 
def findFactors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num // i))
    return factors

def hasFiveHun(num):
    return len(findFactors(num)) > 500
def butt(num):
    return len(findFactors(num)) > 5

num = 0
for i in range(50000):
    if hasFiveHun(num):
        print(num)
        break
    else:
        num = num + i
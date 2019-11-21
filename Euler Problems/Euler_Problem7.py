#Euler Problem 7
import math
def findFactors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num // i))
    return factors

def isPrime(num):
    return len(findFactors(num)) == 2

count = 0
num = 2
while count < 10001:
    if isPrime(num):
        count += 1
        num += 1
    else:
        num += 1
print(num - 1)

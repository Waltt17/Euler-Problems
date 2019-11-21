#Project Euler Problem 3
import math
num = 600851475143
test = 13195

def findFactors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num // i))
    return factors

def isPrime(num):
    return len(findFactors(num)) == 2

facts = findFactors(num)
largest = 0
for fact in facts:
    if isPrime(fact) and fact > largest:
        largest = fact
print(largest)
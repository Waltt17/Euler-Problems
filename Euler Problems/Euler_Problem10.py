#Euler Problem 10
#import math
#def findFactors(num):
#    factors = []
#    for i in range(1, int(math.sqrt(num)) + 1):
#        if num % i == 0:
#            factors.append(i)
#            factors.append(int(num // i))
#    return factors

#def isPrime(num):
#    return len(findFactors(num)) == 2

#sum = 0
#for i in range(2, 2000000):
#    if isPrime(i):
#        sum = sum + i
#print(sum)

marked = [0] * 2000000
value = 3
s = 2
while value < 2000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 2000000:
            marked[i] = 1
            i += value
    value += 2
print(s)
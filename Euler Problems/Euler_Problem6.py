#Euler Problem 6

sumSquare = 0
squareSum = 0
for i in range(1,101):
    sumSquare = sumSquare + (i ** 2)
    squareSum = squareSum + i
squareSum = squareSum ** 2
print(sumSquare)
print(squareSum)

total = squareSum - sumSquare
print(total)
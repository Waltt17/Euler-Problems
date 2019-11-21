#Euler Problem 5

def isDivisible(x):
    for i in range(1, 21):
        if x % i != 0:
            return False
    return True

number = 1
while isDivisible(number) == False:
    number += 1

print(number)
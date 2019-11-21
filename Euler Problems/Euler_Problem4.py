#Project Euler Problem 4

highest = 999 * 999
lowest = 100 * 100

def isPal(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        return True
    else:
        return False
    return

biggest = 0
for i in range(100, 1000):
   for j in range(100, 1000):
       if isPal(i * j) and (i * j) > biggest:
           biggest = i * j

print(biggest)
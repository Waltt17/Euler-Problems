#Project Euler Problem 1

def euler1(x):
   sum = 0

   for x in range(x):
       if (x % 3 == 0) & (x % 5 == 0):
           sum  = sum + x
           continue
       elif(x % 5 == 0):
           sum = sum + x
           continue
       elif(x % 3 == 0):
           sum = sum + x
           continue
       else:
           continue
   return sum

num = int(input())
num = euler1(num)
print(num)
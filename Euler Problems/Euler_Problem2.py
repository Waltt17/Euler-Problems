#Project Euler Problem 2

def fib():
    fib = [1, 2]
    curr = fib[0] + fib[1]
    track = 1
    while curr <= 4000000:
        fib.append(curr)
        curr = curr + fib[track]
        track = track + 1
        continue
    return fib

def euler2(x):
    sum = 0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            sum = sum + x[i]
            continue
        continue
    return sum

fibList = fib()
ans = euler2(fibList)
print(ans)

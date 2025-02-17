def collatz(n):
    if (n == 1):
        return None
    elif ( n % 2 == 0):
        print(n//2)
        collatz(n // 2)
    else:
        print(3*n+1)
        collatz(3 * n + 1)

collatz(10)
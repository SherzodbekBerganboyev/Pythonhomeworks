def p(n):
    if n == 2: return True
    elif n < 2 or n % 2 == 0: return False
    else:
        i = 3
        while i*i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

for i in range(1, 101):
    if p(i):
        print(i, end=" ")
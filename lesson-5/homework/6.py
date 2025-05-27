def is_prime(n):
    if n == 2: return True
    elif n < 2 or n % 2 == 0: return False
    else:
        i = 3
        while i*i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

print(is_prime(19))
def is_palindrome(tup):
    return tup == tup[::-1]

print(is_palindrome((1, 2, 3, 2, 1)))  # True
print(is_palindrome((1, 2, 3)))        # False

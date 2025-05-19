def second_largest(tup):
    unique = set(tup)
    unique.remove(max(unique))
    return max(unique)

my_tuple = (4, 1, 7, 7, 5)
print(second_largest(my_tuple))  # Natija: 5

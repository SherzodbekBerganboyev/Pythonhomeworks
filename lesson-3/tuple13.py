def second_smallest(tup):
    unique = set(tup)
    unique.remove(min(unique))
    return min(unique)

my_tuple = (4, 1, 7, 7, 5)
print(second_smallest(my_tuple))  # Natija: 4

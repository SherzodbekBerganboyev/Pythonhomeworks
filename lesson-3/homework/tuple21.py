def repeat_elements(tup, n):
    return tuple(element for element in tup for _ in range(n))

my_tuple = (1, 2, 3)
repeated = repeat_elements(my_tuple, 3)
print(repeated)  # Natija: (1, 1, 1, 2, 2, 2, 3, 3, 3)

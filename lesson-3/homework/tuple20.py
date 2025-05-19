def create_nested_tuple(tup, size):
    return tuple(tup[i:i+size] for i in range(0, len(tup), size))

my_tuple = (1, 2, 3, 4, 5, 6, 7)
nested = create_nested_tuple(my_tuple, 3)
print(nested)  # Natija: ((1, 2, 3), (4, 5, 6), (7,))

def find_all_indices(tup, element):
    return [i for i, x in enumerate(tup) if x == element]

my_tuple = (1, 2, 3, 2, 4, 2)
indices = find_all_indices(my_tuple, 2)
print(indices)  # Natija: [1, 3, 5]

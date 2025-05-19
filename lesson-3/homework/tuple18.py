def min_of_subtuple(tup, start, end):
    return min(tup[start:end])

my_tuple = (1, 5, 2, 8, 3)
print(min_of_subtuple(my_tuple, 1, 4))  # Natija: 2

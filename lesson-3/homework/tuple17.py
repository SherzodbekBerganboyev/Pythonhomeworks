def max_of_subtuple(tup, start, end):
    return max(tup[start:end])

my_tuple = (1, 5, 2, 8, 3)
print(max_of_subtuple(my_tuple, 1, 4))  # Natija: 8 (indeks 1 dan 3 gacha)

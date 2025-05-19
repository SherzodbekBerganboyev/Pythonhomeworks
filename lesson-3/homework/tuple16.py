def is_sorted(tup):
    return all(tup[i] <= tup[i+1] for i in range(len(tup)-1))

print(is_sorted((1, 2, 2, 4)))  # True
print(is_sorted((3, 2, 1)))     # False

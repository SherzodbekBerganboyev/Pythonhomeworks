def unique_elements(tup):
    seen = set()
    result = []
    for item in tup:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return tuple(result)

my_tuple = (1, 2, 2, 3, 1, 4)
print(unique_elements(my_tuple))  # Natija: (1, 2, 3, 4)

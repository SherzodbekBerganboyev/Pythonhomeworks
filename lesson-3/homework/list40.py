my_list = [1, 2, 2, 3, 1, 4]
seen = set()
unique_ordered = [x for x in my_list if not (x in seen or seen.add(x))]
print(unique_ordered)  # Natija: [1, 2, 3, 4]

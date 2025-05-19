my_list = [1, 2, 2, 3, 1, 4]
unique_list = []
for x in my_list:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)  # Natija: [1, 2, 3, 4]

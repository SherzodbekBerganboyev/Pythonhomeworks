my_list = [1, 2, 3, 4, 5, 6]
group_size = 2
nested = [my_list[i:i+group_size] for i in range(0, len(my_list), group_size)]
print(nested)  # Natija: [[1, 2], [3, 4], [5, 6]]

my_list = [1, 2, 3]
repeat = 2
repeated_list = [x for x in my_list for _ in range(repeat)]
print(repeated_list)  # Natija: [1, 1, 2, 2, 3, 3]

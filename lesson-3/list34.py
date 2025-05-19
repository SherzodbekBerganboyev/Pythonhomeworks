my_list = [1, 2, 3, 4, 5]
shift = 2  # 2 ta o‘ngga siljitish
rotated = my_list[-shift:] + my_list[:-shift]
print(rotated)  # Natija: [4, 5, 1, 2, 3]

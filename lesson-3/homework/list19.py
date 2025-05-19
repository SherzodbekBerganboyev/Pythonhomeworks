my_list = [1, 2, 3, 2]
old = 2
new = 99

if old in my_list:
    index = my_list.index(old)
    my_list[index] = new

print(my_list)  # Natija: [1, 99, 3, 2]

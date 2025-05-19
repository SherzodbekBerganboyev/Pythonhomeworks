my_list = [1, 2, 3, 4]
n = len(my_list)
if n == 0:
    middle = None
elif n % 2 == 0:
    middle = my_list[n//2 - 1:n//2 + 1]
else:
    middle = my_list[n//2]
print(middle)  # Natija: [2, 3]

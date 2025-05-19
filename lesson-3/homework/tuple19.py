def remove_element(tup, element):
    lst = list(tup)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

my_tuple = (1, 2, 3, 2, 4)
print(remove_element(my_tuple, 2))  # Natija: (1, 3, 2, 4)

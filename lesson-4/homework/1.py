list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 3, 6, 6, 7]
commons = set(list1) & set(list2)
uncoms = []
for i in list2 + list1:
    if not i in commons:
        uncoms.append(i)
if uncoms == []:
    print("hamma elementlar umumiy")
else:
    print(uncoms)


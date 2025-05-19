my_dict = {"b": 2, "a": 3, "c": 1}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)  # {'c': 1, 'b': 2, 'a': 3}

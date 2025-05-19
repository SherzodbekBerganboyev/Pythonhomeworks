my_dict = {"a": 1, "b": 2, "c": 3}
filtered = {k: v for k, v in my_dict.items() if v > 1}
print(filtered)  # {'b': 2, 'c': 3}

my_dict = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in my_dict.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}

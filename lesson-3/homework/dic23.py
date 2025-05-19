dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
has_common = bool(set(dict1.keys()) & set(dict2.keys()))
print(has_common)  # True

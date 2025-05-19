my_dict = {"a": 1, "b": {"x": 10}}
has_nested = any(isinstance(v, dict) for v in my_dict.values())
print(has_nested)  # True

from collections import defaultdict

d = defaultdict(lambda: 0)
d["a"] += 1
print(d["a"])  # 1
print(d["b"])  # 0 (default)

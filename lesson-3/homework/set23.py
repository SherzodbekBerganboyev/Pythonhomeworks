import random

def generate_random_set(size, start, end):
    result_set = set()
    while len(result_set) < size:
        result_set.add(random.randint(start, end))
    return result_set

random_set = generate_random_set(5, 1, 20)
print(random_set)  # Tasodifiy 5 ta noyob son

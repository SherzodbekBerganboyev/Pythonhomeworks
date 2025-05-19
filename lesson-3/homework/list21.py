numbers = [5, 2, 9, 1, 1]
unique_sorted = sorted(set(numbers))
second_smallest = unique_sorted[1] if len(unique_sorted) > 1 else None
print(second_smallest)  # Natija: 2

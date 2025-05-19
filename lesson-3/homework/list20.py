numbers = [5, 2, 9, 1, 5]
unique_sorted = sorted(set(numbers), reverse=True)
second_largest = unique_sorted[1] if len(unique_sorted) > 1 else None
print(second_largest)  # Natija: 5

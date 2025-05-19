def is_sublist(main_list, sublist):
    n = len(sublist)
    return any(main_list[i:i+n] == sublist for i in range(len(main_list) - n + 1))

# Misol:
main = [1, 2, 3, 4, 5]
sub = [3, 4]
print(is_sublist(main, sub))  # Natija: True

sub = [2, 5]
print(is_sublist(main, sub))  # Natija_

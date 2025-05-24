password = input("Pasword: ")
def check(password):
    if len(password) < 8:
        return "Too short"
    for i in set(password):
        if i == i.upper() and not i.isdigit():
            break
    else:
        return "Password must contain an uppercase letter"
    return "Password is strong"
print(check(password))
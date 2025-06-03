def check(func):
    def wrapper(n, m):
        if m == 0:
            print("Bo‘luvchi nol bo‘lishi mumkin emas!")
            return
        return func(n, m)
    return wrapper

@check
def div(n, m):
    print(n / m)

n = int(input("Birinchi sonni kiriting: "))
m = int(input("Ikkinchi sonni kiriting: "))

div(n, m)

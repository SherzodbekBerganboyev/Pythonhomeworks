def check(func):
    def fn(a, b):
        if b != 0:
            func(a, b)
        else:
            return "Denominator can't be zero"
    return fn

@check
def div(a, b):
    return a / b
print(div(2, 0))
def convert_cel_to_far(c):
    return c * 9/5 + 32

def convert_far_to_cel(f):
    return (f - 32) * 5/9

f = int(input("Enter a temperature in degrees F: "))
print(f"{f} degress F = {convert_far_to_cel(f): .2f} degrees C")
c = int(input("Enter a temperature in degrees C: "))
print(f"{c} degress C = {convert_cel_to_far(f): .2f} degrees F")
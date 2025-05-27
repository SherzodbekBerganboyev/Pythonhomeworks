universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(data):
    return [[i[1] for i in data], [i[2] for i in data]]
def mean(a):
    return float(format(sum(a) / len(a), '.2f'))

def median(a):
    a.sort()
    l = len(a)
    return a[l//2]
x = 0
print("******************************")
for i in enrollment_stats(universities):
    if x == 0:
        print(f"Total students: {sum(i):,}")
        x = 1
    else:
        print(f"Total tuition: ${sum(i):,}")
x = 0
print()
for i in enrollment_stats(universities):
    if x == 0:
        print(f"Student mean: {mean(i):,}")
        print(f"Student median: {median(i):,}")
        x = 1
    else:
        print()
        print(f"Tuition mean: {mean(i):,}")
        print(f"Tuition median: {median(i):,}")
print("******************************")

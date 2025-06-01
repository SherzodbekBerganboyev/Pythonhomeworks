from collections import Counter
FILE = 'C:/Users/sherz/OneDrive/Desktop/codes/Python/Pythonhomeworks/lesson-6/homework/sample.txt'

def total():
    file = open(FILE, 'r')
    text = file.read().replace('.', '').replace(',', '.')
    c = Counter(text.lower().split())
    print("Total words:", len(c.keys()))
    text = file.read().replace('.', '').replace(',', '.')
    c = Counter(text.lower().split())
    for k, v in c.items():
        print(k, "-", v, 'times')

def wr():
    s = input("write in one line:")
    f = open(FILE, 'w')
    f.write(s)
    f.close()
    print("writted!")

def top():
    n = int(input("how many common words: "))
    file = open(FILE, 'r')
    text = file.read().replace('.', '').replace(',', '.')
    c = Counter(text.lower().split())
    for k, v in c.most_common(n):
        print(k, "-", v, 'times')


def hlp():
    print("""h - help
c - get most common words
w - write your own text
t - total
q - quit
    """)
running = True
hlp()
while running:
    command = input(">>$ ")
    if command == 'q':
        running = False
        break
    elif command == 'h':
        hlp()
    elif command == 't':
        total()
    elif command == 'c':
        top()
    elif command == 'w':
        wr()
    else:
        print('command not found')

print("bye")
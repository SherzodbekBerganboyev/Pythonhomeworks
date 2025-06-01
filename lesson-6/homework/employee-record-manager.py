FILE = 'C:/Users/sherz/OneDrive/Desktop/codes/Python/Pythonhomeworks/lesson-6/homework/employees.txt'

def add_employee(name, position, salary):
    with open(FILE, 'a') as f:
        f.write('\n' + ', '.join(
                [str(id(name + position + str(salary))), name, position, str(salary)]
            )
        )
    print("------ EMPLOYEE ADDED ------\n")

def view():
    print("------ VIEW ALL ------")
    with open(FILE, 'r') as f:
        for line in f.readlines():
            print(line, end='')
    print("----------------------\n")


def search(eid):
    eid = str(eid)
    with open(FILE, 'r') as f:
        for line in f.readlines():
            if line[:line.index(',')] == eid:
                return line
    return "EMPLOYEE NOT FOUND"

def update(eid, name, position, salary):
    print("------ EMPLOYEE DATA UPDATED ------\n")
    text = ""
    with open(FILE, 'r') as f:
        for line in  f.readlines():
            if line.split(', ')[0] == str(eid):
                text += ', '.join([str(eid), name, position, str(salary)]) + "\n"
                continue
            text += line
    f = open(FILE, 'w')
    f.write(text)
    f.close()
    return True

def delete(eid):
    print("------ EMPLOYEE DELETED ------\n")
    text = ""
    with open(FILE, 'r') as f:
        for line in  f.readlines():
            if line.split(', ')[0] == str(eid):
                continue
            text += line
    f = open(FILE, 'w')
    f.write(text)
    f.close()
    return True

# add_employee("Asadbek", "Backend developer", 50000)

view()
update(140289708755344, "Asadbek", "Backend developer", 10000)
view()

delete(140289708755344)
view()

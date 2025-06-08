class Employee:
    def __init__(self, employee_id, name,position,salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
class EmployeeManager:
    def __init__(self):
        self.filename = "employees.txt"
    def add_employee(self, employee):
        with open(self.filename, "a") as file:
            file.write(f"{employee.employee_id},{employee.name},{employee.position},{employee.salary}\n")
        print("Employee added successfully!")
    def view_employee(self):
        with open(self.filename) as file:
            text = file.read()
            print(text)
    def search_employee(self, employee_id):
        employee_id = input("Enter employee ID: ")
        with open(self.filename) as file:
            lines = file.readlines()
            found = False
            for line in lines:
                data = line.strip().split(",")
                if employee_id == data[0]:
                    print(line)
                    found = True
                    break
            if not found:
                print("Employee not found!")

    def update_employee(self):
        employee_id = input("Enter employee ID: ")
        found = False

        with open(self.filename, "r") as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            data = line.strip().split(",")
            if employee_id == data[0]:
                new_employee_id = input("Enter new employee ID: ")
                new_employee_name = input("Enter new employee name: ")
                new_employee_position = input("Enter new employee position: ")
                new_employee_salary = input("Enter new employee salary: ")
                updated_line = f"{new_employee_id},{new_employee_name},{new_employee_position},{new_employee_salary}\n"
                new_lines.append(updated_line)
                found = True
                print("Employee updated successfully!")
            else:
                new_lines.append(line)

        if found:
            with open(self.filename, "w") as file:
                file.writelines(new_lines)
        else:
            print("Employee not found!")

    def delete_employee(self):
        employee_id = input("Enter employee ID: ")
        found = False

        with open(self.filename, "r") as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            data = line.strip().split(",")
            if employee_id == data[0]:
                found = True
                print("Employee deleted successfully!")
                continue  # bu qatorni faylga yozmaymiz (o‘chiriladi)
            new_lines.append(line)

        if found:
            with open(self.filename, "w") as file:
                file.writelines(new_lines)
        else:
            print("Employee not found!")


manager = EmployeeManager()

while True:
    answer1 = input('''
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
Enter your choice: ''')

    if answer1 == '6':
        print("Goodbye!")
        break
    elif answer1 == '1':
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        employee = Employee(employee_id, name, position, salary)
        manager.add_employee(employee)
    elif answer1 == '2':
        manager.view_employee()
    elif answer1 == '3':
        manager.search_employee()
    elif answer1 == '4':
        manager.update_employee()
    elif answer1 == '5':
        manager.delete_employee()
    else:
        print("Invalid input!")










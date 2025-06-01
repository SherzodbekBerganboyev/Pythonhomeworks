
import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self, employee):
        if self.find_employee(employee.employee_id):
            print("Employee ID already exists.")
            return
        with open(self.filename, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        if not os.path.exists(self.filename):
            print("No records found.")
            return
        with open(self.filename, "r") as file:
            for line in file:
                print(line.strip())

    def find_employee(self, employee_id):
        if not os.path.exists(self.filename):
            return None
        with open(self.filename, "r") as file:
            for line in file:
                if line.startswith(str(employee_id)):
                    return line.strip()
        return None

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated = False
        lines = []
        if not os.path.exists(self.filename):
            print("File not found.")
            return
        with open(self.filename, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if parts[0] == str(employee_id):
                    parts[1] = name or parts[1]
                    parts[2] = position or parts[2]
                    parts[3] = salary or parts[3]
                    updated = True
                    lines.append(", ".join(parts))
                else:
                    lines.append(line.strip())
        with open(self.filename, "w") as file:
            for line in lines:
                file.write(line + "\n")
        if updated:
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self, employee_id):
        deleted = False
        lines = []
        if not os.path.exists(self.filename):
            print("File not found.")
            return
        with open(self.filename, "r") as file:
            for line in file:
                if not line.startswith(str(employee_id)):
                    lines.append(line.strip())
                else:
                    deleted = True
        with open(self.filename, "w") as file:
            for line in lines:
                file.write(line + "\n")
        if deleted:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def run(self):
        while True:
            print("\n1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                self.add_employee(Employee(employee_id, name, position, salary))
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                result = self.find_employee(employee_id)
                print("Employee Found:" if result else "Not found.")
                if result:
                    print(result)
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new name (press enter to skip): ")
                position = input("Enter new position (press enter to skip): ")
                salary = input("Enter new salary (press enter to skip): ")
                self.update_employee(employee_id, name, position, salary)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

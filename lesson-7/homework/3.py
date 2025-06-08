import csv
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date="", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class TaskStorageCSV:
    def __init__(self, filename):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["TaskID", "Title", "Description", "DueDate", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load_tasks(self):
        tasks = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(
                        task_id=row["TaskID"],
                        title=row["Title"],
                        description=row["Description"],
                        due_date=row["DueDate"],
                        status=row["Status"]
                    )
                    tasks.append(task)
        except FileNotFoundError:
            pass  # Fayl mavjud bo'lmasa, bo'sh ro'yxat qaytadi
        return tasks

class ToDoApp:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD) (optional): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        new_task = Task(task_id, title, description, due_date, status)
        self.tasks.append(new_task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input(f"Enter new Title ({task.title}): ") or task.title
                task.description = input(f"Enter new Description ({task.description}): ") or task.description
                task.due_date = input(f"Enter new Due Date ({task.due_date}): ") or task.due_date
                task.status = input(f"Enter new Status ({task.status}): ") or task.status
                print("Task updated successfully!")
                return
        print("Task not found!")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found!")

    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if filtered:
            for task in filtered:
                print(task)
        else:
            print(f"No tasks found with status '{status}'.")

    def save_tasks(self):
        self.storage.save_tasks(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load_tasks()
        print("Tasks loaded successfully!")

def main():
    storage = TaskStorageCSV("tasks.csv")  # CSV formatda saqlashni ishlatamiz
    app = ToDoApp(storage)

    while True:
        print("""
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
""")
        choice = input("Enter your choice: ")

        if choice == '1':
            app.add_task()
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            app.update_task()
        elif choice == '4':
            app.delete_task()
        elif choice == '5':
            app.filter_tasks()
        elif choice == '6':
            app.save_tasks()
        elif choice == '7':
            app.load_tasks()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

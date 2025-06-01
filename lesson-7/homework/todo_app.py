
import json
import csv
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class TaskManager:
    def __init__(self, storage_format="json"):
        self.tasks = []
        self.storage_format = storage_format
        self.filename = f"tasks.{storage_format}"

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = kwargs.get("title", task.title)
                task.description = kwargs.get("description", task.description)
                task.due_date = kwargs.get("due_date", task.due_date)
                task.status = kwargs.get("status", task.status)
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        for task in self.tasks:
            if task.status == status:
                print(task)

    def save_tasks(self):
        if self.storage_format == "json":
            with open(self.filename, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f)
        elif self.storage_format == "csv":
            with open(self.filename, "w", newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
                writer.writeheader()
                for task in self.tasks:
                    writer.writerow(task.to_dict())

    def load_tasks(self):
        self.tasks = []
        try:
            if self.storage_format == "json":
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    for item in data:
                        self.tasks.append(Task(**item))
            elif self.storage_format == "csv":
                with open(self.filename, "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.tasks.append(Task(**row))
        except FileNotFoundError:
            print("No saved tasks found.")

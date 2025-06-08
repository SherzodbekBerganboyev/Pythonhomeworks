import json
import csv

def load_tasks(filename="tasks.json"):
    with open(filename, 'r') as file:
        tasks = json.load(file)
    return tasks

def display_tasks(tasks):
    print("ID | Task Name       | Completed | Priority")
    print("--------------------------------------------")
    for t in tasks:
        print(f"{t['id']:2} | {t['task']:<15} | {t['completed']}      | {t['priority']}")

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(t['completed'] for t in tasks)
    pending = total - completed
    avg_priority = sum(t['priority'] for t in tasks) / total if total else 0
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {avg_priority:.2f}")

def convert_to_csv(tasks, csv_filename="tasks.csv"):
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for t in tasks:
            writer.writerow([t['id'], t['task'], t['completed'], t['priority']])
    print(f"Tasks saved to {csv_filename}")

# Example usage:
tasks = load_tasks()
display_tasks(tasks)
calculate_stats(tasks)
# Suppose you modify tasks here if needed...
save_tasks(tasks)
convert_to_csv(tasks)

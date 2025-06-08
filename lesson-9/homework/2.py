import csv
from collections import defaultdict

# Step 1: Read grades.csv
grades = []
with open("grades.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Grade'] = int(row['Grade'])
        grades.append(row)

# Step 2: Calculate average grade per subject
subject_totals = defaultdict(int)
subject_counts = defaultdict(int)

for entry in grades:
    subject_totals[entry['Subject']] += entry['Grade']
    subject_counts[entry['Subject']] += 1

average_grades = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# Step 3: Write average_grades.csv
with open("average_grades.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in average_grades.items():
        writer.writerow([subject, round(avg, 1)])

print("Average grades calculated and saved to average_grades.csv")

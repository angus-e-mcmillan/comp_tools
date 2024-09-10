import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many comand-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few comand-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

filetype = (input_file.split("."))
if filetype[1] != "csv":
    sys.exit("Not a CSV file")

students = []
try:
    with open(input_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})
except FileNotFoundError:
    sys.exit("File does not exist")

for student in students:


print(students)

with open(output_file, "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": row["name"], "house": row["house"]})

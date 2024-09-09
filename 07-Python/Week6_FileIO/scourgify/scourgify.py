import sys

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
        for line in file:
            student = line.rstrip().split(",")
            students.append(student)
except FileNotFoundError:
    sys.exit("File does not exist")



print(students)
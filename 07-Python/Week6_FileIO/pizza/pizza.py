import sys
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many comand-line arguments")
elif len(sys.argv) == 1:
    sys.exit("Too few comand-line arguments")

program = sys.argv[1]
filetype = (program.split("."))
if filetype[1] != "csv":
    sys.exit("Not a CSV file")

menu = []
try:
    with open(program, "r") as file:
        for line in file:
            pizza, small, large = line.rstrip().split(",")
            menu.append(f"{pizza}. {small}, {large}")
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(menu, tablefmt="grid"))
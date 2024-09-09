import sys

if len(sys.argv) > 2:
    sys.exit("Too many comand-line arguments")
elif len(sys.argv) == 1:
    sys.exit("Too few comand-line arguments")

program = sys.argv[1]
filetype = (program.split("."))
if filetype[1] != "py":
    sys.exit("Not a Python file")

lines = []
try:
    with open(program, "r") as file:
        for line in file:
            lines.append(line.rstrip())
except FileNotFoundError:
    sys.exit("File does not exist")

l = 0
for line in lines:
    if line[0] == "#":
        pass
    elif (line[0] == " ") and (line[1] == "#"):
        pass
    else:
        l = l + 1

print(l)
#try and except for finding errors
try:
    x = int(input("what is x"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
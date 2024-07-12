def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if length < 3:
        print("Invalid")
    elif length > 6:
        print("Invalid")
    else:
        print("Valid")


main()
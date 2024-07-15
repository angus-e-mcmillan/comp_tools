def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if length < 3:
        print("Invalid_short")
        return False
    elif length > 6:
        print("Invalid_long")
        return False
    elif s.isalnum() != True:
        print("Invalid_punct")
        return False
    elif (s[0].isdigit()) and ((s[1:]).isalpha() is False):
        print("Invalid_slice1")
        return False
    elif (s[1].isdigit()) and ((s[2:]).isalpha() is False):
        print("Invalid_slice2")
        return False
    elif (s[2].isdigit()) and ((s[3:]).isalpha() is False):
        print("Invalid_slice3")
        return False
    elif (s[3].isdigit()) and ((s[4:]).isalpha() is False):
        print("Invalid_slice2")
        return False
    elif (s[4].isdigit()) and ((s[5:]).isalpha() is False):
        print("Invalid_slice1")
        return False
    elif (s[5].isdigit()) and ((s[6:]).isalpha() is False):
        print("Invalid_slice2")
        return False
    else:
        return True
main()


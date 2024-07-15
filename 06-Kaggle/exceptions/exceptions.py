#try and except for finding errors
#def main():
#    x = get_int()
#    print(f"x is {x}")
    
# def get_int():
#    while True:
#        try:
#            return int(input("what is x"))
#        except ValueError:
#            print("x is not an integer")

#main()

#Pass allows us to pass and remain inside a loop
def main():
    x = get_int("What is x?")
    print(f"x is {x}")
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
           pass

main()
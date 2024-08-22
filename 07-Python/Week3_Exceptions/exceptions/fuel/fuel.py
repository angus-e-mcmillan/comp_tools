def main():
    fuel = get_int("Fuel: ")
    if fuel < 1:
        print("E")
    elif fuel > 99:
        print("F")
    else:
        print(f"{fuel}%")

def get_int(prompt):
    while True:
        try:
            fraction = (input(prompt))
            fraction = fraction.split("/")
            x = int(fraction[0])
            y = int(fraction[1])
            return int((x/y)*100)
        except ValueError or ZeroDivisionError:
           pass

main()
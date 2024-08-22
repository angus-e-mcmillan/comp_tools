menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
item = "Nothing"
try:
    while item != "-d":
        item = (input("Item: ")).title()
        purchase = menu.get(item)
        total = total + purchase
        print(f"Total: {total}")
except TypeError:
    pass
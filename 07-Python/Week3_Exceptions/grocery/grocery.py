#Initial state
groceries = {}
item = "nothing"
n = 1

#Loop to build dictionary of items, keeping count of how many times an item is added
while True:
    try:
        item = (input("item: ")).upper()
        if item == "-D":
            break
        groceries.update({n: item})
        n = n + 1

#Sort the dictionary alphabetically


#Print the dictionary
print(groceries)
coke = 50
paid = 0
while paid < 50:
    coin = int(input("Insert Coin:"))
    paid = paid + coin
    due = coke - paid
    print("Amount due:", due)
if paid >= 50:
    print("Change owed:", (paid - coke))
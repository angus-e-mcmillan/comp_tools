import inflect
p = inflect.engine()

names = []
while True:
   x = input("Name: ")
   if x == "-d":
        break
   else:
       names.append(x)
       
mylist = p.join()
print("Adieu, adieu, to " + mylist)
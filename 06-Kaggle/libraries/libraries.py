#Code you can use or share using modules
#Python comes with a "random" library
#use functions from this library
#use import

#import random
#coin = random.choice(["heads", "tails"])
#print(coin)

#from random import choice
#coin = random.choice(["heads", "tails"])
#print(coin)

#import random
#number = random.randint(1, 10)
#print(number)

#import random
#cards = ["jack", "queen", "king"]
#random.shuffle(cards)
#for card in cards:
#    print(card)

#import statistics
#print(statistics.mean([100, 90]))

#command-line arguments

#import sys
#print("Hello, my name is", sys.argv[1])
#Why 1? What is in [0], well it is the name of the file your executing
#If we don't add our name we get indexerror: list index out of range

import sys
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
31:30
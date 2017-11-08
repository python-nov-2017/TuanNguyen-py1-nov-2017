import random

head = 0
tail = 0

print "Starting the program..."
for i in xrange(5001):
    coin = round(random.random())
    if coin == 0:
        head+=1
    else:
        tail+=1
    print "Attempt #", i, ": Throwing a coin... It's a", "head" if coin ==0 else "tail", "! ... Got", head, "head(s) so far and", tail,"tail(s) so far"

print "Ending the programe, thank you!"
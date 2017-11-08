print "Multiples"
for i in range(1,1000):
    if i%2 == 1:
        print i
for i in range(5,1000000):
    if i%5 == 0:
        print i

print "\nSum List"
a = [1, 2, 5, 10, 255, 3]
print sum(i for i in a)

print "\nAverage List"
a = [1, 2, 5, 10, 255, 3]
print sum(i for i in a) / len(a)
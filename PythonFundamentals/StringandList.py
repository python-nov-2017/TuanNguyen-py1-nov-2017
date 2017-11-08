print "Find and Replace"
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
new_words = words.replace("day", "month",1)
print new_words

print "\nMin and Max"
x = [2,54,-2,7,12,98]
print "Min value in list x is: ", min(x)
print "Max value in list x is: ", max(x)

print "\nFirst and Last"
x = ["hello",2,54,-2,7,12,98,"world"]
y = [x[0], x[len(x)-1]]
print y

print "\nNew List"
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = []
count = 0
size = len(x)/2 -1
while count <= size:
    y.append(x[0])
    x.pop(0)
    count+=1
x.insert(0,y)
print y    
print x


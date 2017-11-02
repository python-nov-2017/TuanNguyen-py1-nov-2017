row = 13
col = 13
for i in range(0,row):
    for j in range(0, col):
        if i == 0:
            if j == 0:
                print "   x",
            else: 
                print "{:4}".format(j),
        else:
            if j == 0:
                print "{:4}".format(i),            
            else:    
                print "{:4}".format(i*j),
    print ""


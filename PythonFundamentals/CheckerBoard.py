row = 10
col = 8
for i in range(1,row):
    for j in range(1,col):
        if (i+j)%2 == False:
            print "*",
        else:
            print " ",
    print ""


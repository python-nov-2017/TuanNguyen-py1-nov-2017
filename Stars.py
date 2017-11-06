# x = [4, 6, 1, 3, 5, 7, 25]
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


for i in x:
    if type(i) is int:
        for j in range(i):
            print "*",
    if type(i) is str:
        for j in i:
            print i[0].lower(),    
    print ""
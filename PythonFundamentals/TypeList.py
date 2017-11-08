#input
l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
# l = ['magical','unicorns']

#output
if all(isinstance(i,(int, long, float, complex)) for i in l):
    print "The list you entered is of integer type"
    print "Sum:", sum(i for i in l)
elif all(isinstance(i,basestring) for i in l):
    print "The list you entered is of string type"
    print "String: " + " ".join(l)
else:
    print "The list you entered is of mixed type"
    num = 0
    s = ''
    for i in l:
        if isinstance(i, (int, long, float, complex)):
            num+=i
        if isinstance(i, basestring):
            s+=" " + i
    print "String:", s
    print "Sum:", num
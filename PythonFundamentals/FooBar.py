def isPrime(num):
    return all(num % i for i in xrange(2, num))

def isSquare(num):
    return any((i*i)==num for i in xrange(int(num/2)+1))
    # for i in xrange(int(n/2)+1):
    #     if (i*i) == n:
    #         return True
    #     else:
    #         return False


for i in xrange(100, 100000):
    if isPrime(i):
        print i, " Foo"    
    if isSquare(i):
        print i, " Bar"
    else:
        print "FooBar"
    
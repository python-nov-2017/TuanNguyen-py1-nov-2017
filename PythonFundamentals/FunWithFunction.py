print "Odd/Even"
for i in xrange(1,2001):
    if i % 2 == 0:
        print "Number is ", i, ". This is an even number."
    else:
        print "Number is ", i, ". This is an odd number."



print "\nMultiply"
def multiply(arr, num):
    for i in xrange(len(arr)):
        arr[i]*=num
    return arr

a = [2,4,6,8,10]
b = multiply(a,5)
print b


print "\nHacker Challenge"
def layered_multiples(arr):
    new_array = []
    for i in xrange(len(arr)):
        subarray = []
        for j in xrange(arr[i]):
            subarray.append(1)
        new_array.append(subarray)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x


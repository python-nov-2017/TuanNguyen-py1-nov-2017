# my_arr = [1,2,3,4,5]
# map(lambda x: x ** 2, my_arr)


# def invoker(callback):
#     print callback(2)
# invoker(lambda x: 2 * x)
# invoker(lambda y: 5 + y)

class Underscore(object):
    def map(self, arr, callback):
        filter_arr = []
        for item in arr:
            filter_arr.append(callback(item))
        return filter_arr

    def reduce(self, arr, callback, memo=None):     
        for item in arr:
            memo = callback(memo, item)
        return memo

    def find(self, arr, callback):
        for item in arr:
            if callback(item):
                return item

    def filter(self, arr, callback):
        filter_arr = []
        for item in arr:
            if callback(item):
                filter_arr.append(item)
        return filter_arr

    def reject(self, arr, callback):
        filter_arr = []
        for item in arr:
            if not callback(item):
                filter_arr.append(item)
        return filter_arr        

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore

evens = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 2)
print evens
evens = _.reduce([1, 2, 3, 4, 5, 6], lambda memo, num: memo + num, 4)
print evens
evens = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print evens
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print evens
evens = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print evens

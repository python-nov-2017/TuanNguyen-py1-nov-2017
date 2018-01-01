class MathDojo(object):
    def __init__(self,val=None):
        if val is None:
            self.total = 0
        else:
            self.total = val

    def add(self, *args):
        sum = 0
        for item in args:
            if isinstance(item, int) or isinstance(item, float):
                sum += item
            else:
                for i in item:
                    sum += MathDojo().add(i).total  

        self.total += sum
        return self

    def subtract(self, *args):
        sum = 0
        for item in args:
            if isinstance(item, int) or isinstance(item, float):
                sum += item
            else:
                for i in item:
                    sum += MathDojo().add(i).total  
        self.total -= sum
        return self
    
    def result(self):
        print self.total
        return self



md = MathDojo()
md.add(2).add(2, 5).subtract(3, 2).result()
print "=================="
del md
md = MathDojo()
md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()

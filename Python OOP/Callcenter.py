from datetime import datetime

class Call(object):
    unique_id = 0
    def __init__(self, name, phone, reason):
        Call.unique_id += 1
        self.name = name
        self.phone = phone
        self.time = datetime.now()
        self.reason = reason
    
    def display(self):
        print "Unique id:", Call.unique_id
        print "Caller name:", self.name
        print "Caller phone number:", self.phone
        print "Time of call:", self.time.strftime("%I:%M:%S")
        print "Reason for call:", self.reason
        print ""
        return self

call1 = Call("Tuan Nguyen", "123-456-7891", "Customer Service")
call1.display()
call2 = Call("Hang Nguyen", "987-654-3210", "Stock info")
call2.display()
print ""

class CallCenter(object):
    def __init__(self):
        self.calls = []
    @property
    def queue_size(self):
        return len(self.calls)
    def add(self, call):
        self.calls.append(call)
        return self
    def remove(self, *args):
        if len(args) == 0:
            self.calls.pop(0)
        else:
            for index in self.calls:
                for arg in args:
                    if index.phone == arg:                
                        self.calls.remove(index)
        return self
    def info(self):
        for call in self.calls:
            print "Caller name:", call.name
            print "Caller phone number:", call.phone
        print "The queue size is ", self.queue_size
        print ""
        return self

center = CallCenter()
center.add(call1)
center.add(call2)
center.remove("987-654-3210")
center.remove()
center.info()


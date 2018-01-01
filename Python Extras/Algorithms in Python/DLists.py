class DLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DList(object):
    def __init__(self):
        self.head = None
        self.tail = None    

    def PrintAllVals(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next

    def AddBack(self, val):        
        node = DLNode(val)
        if self.tail is not None:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node



    def AddFront(self, val):        
        node = DLNode(val)    
        if self.head is not None:    
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node

    def InsertBefore(self, nextVal, val):
        runner = self.head
        node = DLNode(val)
        if self.head.value == nextVal:
            self.AddFront(val)
        while(runner.next != None):
            if runner.next.value == nextVal:
                node.next = runner.next
                node.prev = runner
                runner.next.prev = node
                runner.next = node                
                break
            else:        
                runner = runner.next   

    def InsertAfter(self, preVal, val):
        runner = self.head
        node = DLNode(val)
        if self.tail.value == preVal:
            self.AddBack(val)            
        while(runner.next != None):
            if runner.value == preVal:
                node.next = runner.next                
                node.prev = runner
                runner.next.prev = node
                runner.next = node
                break
            else:        
                runner = runner.next 

    def RemoveNode(self, val):
        runner = self.head
        while(runner != None):
            if runner.next.value == val:
                temp = runner.next.next
                del runner.next
                runner.next = temp
                temp.prev = runner
                break    
            runner = runner.next

    def PrintAllValsReverse(self):
        runner = self.tail
        while(runner != None):
            print(runner.value)
            runner = runner.prev


list = DList()
list.AddBack('Alice')
list.AddBack('Chad')
list.AddBack('Debra')
list.AddBack('Eric')
list.AddBack('Fred')        


print "PrintAllVal() ============= "
list.PrintAllVals()

list.AddBack('Test Tail')
print "AddBack(val) ============= "
list.PrintAllVals()

list.AddFront('Test Head')
print "AddFront(val) ============= "
list.PrintAllVals()

list.InsertBefore("Debra", "TestInsertBefore")
print "InsertBefore(nextVal, val) ================="
list.PrintAllVals()

list.InsertAfter("Debra", "TestInsertAfter")
print "InsertAfter(preval, val) ================="
list.PrintAllVals()

list.RemoveNode("Debra")
print "RemoveNode(val) ================="
list.PrintAllVals()

print "ReverseList() ================="
list.PrintAllValsReverse()
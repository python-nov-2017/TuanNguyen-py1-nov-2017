class SLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SList(object):
    def __init__(self):
        self.head = None
        self.tail = None    

    def PrintAllVals(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next

    def AddBack(self, val):        
        node = SLNode(val)
        self.tail.next = node
        self.tail = node

    def AddFront(self, val):        
        node = SLNode(val)
        node.next = self.head
        self.head = node

    def InsertBefore(self, nextVal, val):
        runner = self.head
        node = SLNode(val)
        if self.head.value == nextVal:
            self.AddFront(val)
        while(runner.next != None):
            if runner.next.value == nextVal:
                node.next = runner.next
                runner.next = node
                break
            else:        
                runner = runner.next   

    def InsertAfter(self, preVal, val):
        runner = self.head
        node = SLNode(val)
        if self.tail.value == preVal:
            self.AddBack(val)            
        while(runner.next != None):
            if runner.value == preVal:
                node.next = runner.next
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
                break    
            runner = runner.next

    def ReverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')
list.head.next.next.next = SLNode('Eric')
list.head.next.next.next.next = SLNode('Fred')        
list.tail = list.head.next.next.next.next


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

list.ReverseList()
print "ReverseList() ================="
list.PrintAllVals()
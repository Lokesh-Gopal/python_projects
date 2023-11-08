class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL(Node):
    def __init__(self):
        self.head=None
        
    def add(self,x):
        n=Node(x)
        if self.head is None:
            self.head=n
        else:
            t=self.head
            while(t.next is not None):
                t=t.next
            t.next=n
    def display(self):
        p=self.head
        while(p is not None):
            print(p.data)
            p=p.next
    def addAtfirst(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def deleteatlast(self):
        t=self.head
        if self.head is not None:

            while(t.next.next is not None):
                t=t.next
            t.next=None
        
            

'''node=Node(4)
print(node.data)
print(node.next)'''
N=SLL()
N.add(5)
N.add(6)
N.add(7)
N.addAtfirst(9)
N.display()
N.deleteatlast()
N.display()
class Node():
    def __init__(self,data):
       self.data=data
       self.next=None
       self.prev=None
class DLL(Node):
    def __init__(self):
        self.head=None
        self.next=None
    def addatend(self,x):
        node=Node(x)
        if self.head is None:
            self.head=node
            self.prev=None
        else:
            t=self.head
            while(t.next is not None):
                t=t.next
            t.next=node
            node.prev=t
    def display(self):
        t=self.head
        while(t is not None):
            print(t.data)
            t=t.next
    

d=DLL()    
x=int(input())
i=0
while(i<x):
   d.addatend(int(input()))
   i+=1
d.display()

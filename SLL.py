class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL(Node):
    def __init__(self):
        self.head=None
        self.last=None
    def InsertatEnd(self,x):
        temp=Node(x)
        if self.head is None:
            self.head=temp
        else:
            t=self.head
            while(t.next is not None):
                t=t.next
            t.next=temp
    '''def InsertatEnd2(self,x):
        temp=Node(x)
        if self.head is None:
            self.head=temp
            self.last=temp
        else:
            self.last.next=temp
            self.last=temp'''
    
    def Display(self):
        t=self.head
        while(t.next is not None):
            print(t.data,end=' ')
            t=t.next
        print(t.data)
s=SLL()
s.InsertatEnd(10)
s.InsertatEnd(20)
s.InsertatEnd(30)
s.Display()
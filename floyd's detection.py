class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
n1.next.next=n3

head=n1
s=head
f=head
while(head!=None):
    print(head.data,head.next)
    head=head.next 
    while f and f.next:
    s=s.next
    f=f.next.next
    
    if s==f:
        print("cycle exists")
    print("no cycle")    '''


#floyd's detection
def detect_cycle(self):
    slow=self.head
    fast=self.head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            print("cycle exist")
            return
        print("no cycle")

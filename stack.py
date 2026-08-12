class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(item,"pushed into stack")
    def pop(self,item):
        if len(self.stack)==0:
            print("stack overflow")
        else:
            print("popped elements",self.stack.pop())
    def peek(self):
        if len(self.stack)==0:
            print("stack overflow")
        else:
            print("top element",self.stack[-1])                       
    def display(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("stack is",self.stack)
def stack_operations():
    s=Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    s.peek()
    s.pop()  
    s.display()              
stack_operations()
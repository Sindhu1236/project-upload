class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self,item):
        if len(self.stack)==0:
            print("empty")
        else:
            return self.stack.pop()           
    def peek(self,item):
        if len(self.stack)==0:
            print("empty")
        else:
            return self.stack[-1]
    def display(self):
        if len(self.stack)==0:
            print("empty")
        else:
            print(stack)
def stack_operation():
    s=stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    s.peek()
    s.pop()
stack_operation()                    

                    
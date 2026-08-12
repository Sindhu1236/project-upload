def search_stack(stack,target):
    temp=[]
    found=False
    while stack:
        top=stack.pop()
        if top==target:
            found=True
        temp.append(top)
    while temp:
        stack.append(temp.pop())
    return found
stack=[10,20,30,40]
element=20
if search_stack(stack,element):
    print("element is found")
else:
    print("not found")
print("stack after searching element",stack)                        

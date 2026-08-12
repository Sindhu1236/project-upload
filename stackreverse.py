#reverse the stack
'''def reverse_stack(stack):
    temp=[]
    while stack:
        temp.append(stack.pop())
    return temp 
stack=[10,20,30] 
n=reverse_stack(stack)
print(n)'''
# copy of stack
'''def copy_stack(stack):
    temp=[]
    copy=[]
    while stack:
        temp.append(stack.pop())
    while temp:
        val=temp.pop()
        stack.append(val)
        copy.append(val)
    return copy
stack=[10,20,30] 
new_stack=copy_stack(stack)
print("original stack",stack)
print("new stack",new_stack)'''
'''s1=[1,2,3]                  #  copy stack using for loop
s2=[]
for i in s1:
    if i not in s2:
        s2.append(i)
print("original stack",s1)        
print("new stack",s2) ''' 
# stack copy using bulit in function (copy)
'''s1=[1,2,3]
print("original stack",s1)
print("new stack",s1.copy())
'''
# delete the elements in the satck
'''s=[1,2,3]

print(s.clear())'''
# using loop delete the elements in th stack
s=[1,2,3,4]
for i in range(len(s)):
    s.pop()
print(s)    
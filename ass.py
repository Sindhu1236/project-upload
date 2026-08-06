#sum pairs equql to target 
'''a=[2,2,1,6,3]
t=4
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==t:
            print(a[i],a[j])            '''
# sort the array without using built in function
'''a=[5,2,7,8,1,3]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)    
'''
# union of 2 arrays
'''a1=[1,2,3,4,5]
a2=[2,3,5,6,7]
n=[]
for i in a1:
    if i not in n:
        n.append(i)
for i in a2:
    if i not in n:
        n.append(i)
print(n)                
'''
'''a={1,2,3,4,5}
a2={2,3,5,6,7}
print(set.union(a,a2))''' # using set opertions
# non repeating character
'''a="aabbcbb"
feq={}
for i in a:
    if i in feq:
        feq[i]+=1
    else:
        feq[i]=1
for i in a:
    if feq[i]==1:
        print(i)
        break     ''' 
# alternate printing numbers
a=[1,3,2,-3,-4,-2]
n=list(a)
for i in range(len(n)):
    if i>0:
        print(n[::2])
        break
    else:
        print(n[::1])     

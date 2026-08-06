'''a=[1,2,30,5]
for i in a:
    print(i)'''

'''a=[1,2,3]
print(a.insert(0,2))
print(a)'''

'''a=[1,2,3,1,2]
d=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j] and a[i] not in d:
            d.append(i)
print(d)      '''
# second lARGEST NO 
'''a=[1,20,13,14]
print(a.sort())
print(a)
print(a[-2])
print(a[0])'''
# second lARGEST NO 
a=[1,20,30,10,50]
'''l=a[0]
sec=-1
for i in a:
    if i>l:
        sec=l
        l=i
    elif i>sec and i!=l:
        sec=i
print(sec)

'''
'''eve_count=0 # even and odd count
od_count=0
for i in a:
    if i%2==0:
        eve_count+=1
      
    else:
        od_count=+1
print(eve_count)
print(od_count)
'''
a=[1,2,3,4,5]
'''start=0   #reverse of array using slice
end=-1
while start<end:
    t=a[start]
    a[start],a[end]=a[end],a[start]
    start+=1
    end=end-1
print(a)
'''
'print(a[::-1])'#reverse of array using slice
"""key=int(input("enter the key"))
for i in a:
    if key==i:
        print("key found")
        break
else:
    print("key not found")  
     """
# binary search
'''k=int(input("enter key value"))
l=0
h=len(a)-1
for i in a:
    if l<h:
        m=(l+h)//2
        if a[m]==k:
            print("key is found")
            break
        elif a[m]<k:
            l=m+1
        else:
            h=m-1
        print("key is found")
        break
    else:
        print("key not found")          '''             
# move all zeros
'''l=[1,0,0,3]
for i in l:
    if i==0:
        l.append(0)
        l.remove(0)
print(l)        '''
# move all zeros without using built in function
"""a=(input("enter the number"))
non_zero=" "
zero=0
for i in a:
    if i=='0':
        zero+=1
    else:
        non_zero+=i
    result=non_zero('0'*zero)
    print(int(result))        """
#reverse of string
'''a=input("enter the string")
b=a[::-1]
print(b)
if a==b[::-1]:
    print("palindrome")
else:
    print("not palindrome")    '''
# character frequency
'''a=[1,2,3,4,1,1,1]
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(i,freq[i])         '''   
# duplicates
'''a=[1,2,1,3,4]
unique=[]
for i in a:
    if i not in unique:
        print(unique.append(i))
print(unique)    '''    
# sorting
a=[1,12,3,15,8]
'''n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("sorted array",a)            '''
# selection sort
'''n=len(a)
for i in  range(n):
    min_i=i
    for j in range(i+1,n):
        if a[j]<a[min_i]:
            min_i=j
    a[i],a[min_i]=a[min_i],a[i]
print("sorted array",a) 
           '''
# insertion sort
'''n=len(a)
for i in range(1,n):
    k=a[i]
    j=i-1
    while j>=0 and a[j]>k:
        a[j+1]=a[j]
        j-=1
    a[j+1]=k
print("sorted",a)        
'''
# merge
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
                K+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
a=list(map(int,input("enter array elements").split()))
merge_sort(a)
print("sorted array",a)            

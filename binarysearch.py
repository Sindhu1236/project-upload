def bs(a,l,h,k):
    if l>h:
        return -1
    mid=(l+h)//2
    if a[mid]==k:
        return mid
    elif a[mid]>k:
        return bs(a,l,mid-1,k)
    else:
        return bs(a,mid+1,h,k)  
a=list(map(int,input("enyter sorted array").split()))
k=int(input("enter the key"))
i=bs(a,0,len(a)-1,k)
if i!=-1:
    print("found",i) 
else:
    print("not found")     
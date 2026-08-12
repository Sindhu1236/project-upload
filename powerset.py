'''def p_s(n):
    r=[[]]
    for num in n:
        new=[]
        for subset in r:
            new.append(subset+[num])
            r+=new
    return r
print(p_s([1,2,3]))    
'''
#power set
'''a=list(map(int,input("enter the elements").split()))
def subset(a,i,c):
    if i==len(a):
        print(c)
        return
    subset(a,i+1,c+[a[i]])
    subset(a,i+1,c)
subset(a,0,[])    '''
def gp(o,c,output):
    if o==0 and c==0:
        print(output)
        return
    if o>0:
        gp(o-1,c,output+"(")
    if c>o:
        gp(o,c-1,output)    
# 
def solve(board,row,col,n):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==abs(i-row):
            return False
        return True
def solve(board,row,n):
    if row==0:
        print(board)
        return
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row]=col
            solve(board,row+1,n)
n=int(input())
board=[-1]*n
solve(board,0,n)

           
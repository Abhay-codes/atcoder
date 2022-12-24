n=int(input())
l=list(map(int,input().split()))
q=int(input())
for i in range(q):
    l1=list(map(int,input().split()))
    if l1[0]==1:
        k=l1[1]-1 
        l[k]=l1[2]
    else:
        k=l1[1]-1 
        print(l[k])
        
    
 
 

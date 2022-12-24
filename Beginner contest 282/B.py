n , m =map(int,input().split())
l=[]
for i in range(n):
    l1=input()
    l.append(l1)
ans=0
for i in range(n):
    
    for k in range(i+1,n):
        c=0
        for j in range(m):
            if l[i][j]=='o' or l[k][j]=='o':
                c+=1 
        if c==m:
            ans+=1 
print(ans)
                
        
       

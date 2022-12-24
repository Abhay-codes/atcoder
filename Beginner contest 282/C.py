n =int(input())
s=input()
s1=""
c=0 
for i in range(n):
    if s[i]!=",":
        s1+=s[i]
    else:
        if c%2==0:
            s1+='.'
        else:
            s1+=','
    if s[i]=='"':
        c+=1 
print(s1)
    

from collections import defaultdict
s=input() 
n =len(s)
i=0
c=0
while(i<n-1):
    if s[i]=='0' and s[i+1]=='0':
        c+=1 
        i+=2 
    else:
        i+=1
print(n-c)

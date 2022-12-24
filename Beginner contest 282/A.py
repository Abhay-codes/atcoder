k=int(input())
x='A'
s=""
for i in range(k):
    s+=x 
    x=chr(ord(x)+1)
print(s)

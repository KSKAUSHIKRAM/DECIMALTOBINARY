
k=input("enter a number:")
r=k[::-1]
d=0
c=0
for i in r:
    f=int(i)*(2**d)
    d=d+1
    c+=f
print(c)

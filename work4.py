a=input(">>")
a=a.split()
b=[int(x) for x in a]
c=sorted(b)
d=len(c)
p=0
e=0
e1=0
e2=0
for i in c:
    p+=i
    l=p/d
for i in c:
    if i<l:
        e+=1
    if i>l:
        e1+=1
    else:
        e2+=1

print (e)
print (e1)
print(e2,"xiangdeng")



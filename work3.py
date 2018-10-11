a=input(">>")
a=a.split()
b=[int(x) for x in a]
c=sorted(b)
def all_list(c):
    result = {}
    for i in set(c):
        result[i] = c.count(i)
    print (result)
all_list(sorted(c))


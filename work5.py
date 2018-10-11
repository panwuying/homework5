import random
a=[]
for i in range(10):
    a.append(random.randint(0,9))
print(a)
print(set(a))
def all_list(a):
    result = {}
    for i in set(a):
        result[i] = a.count(i)
    print (result)
all_list(a)


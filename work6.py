a="4 4  213 123 124 1 123 "
a=a.split()
a=[int(x) for x in a]
def all_list(b):
    c = min(b)
    for i in range(len(b)):
        if c==b[i]:
            print(i)
            break
all_list(a)

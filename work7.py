import random
a=[11,88,737,388,556,667,2424,1,2,3]
def suiji(a):
    b={}
    for i in range(len(a)):
        b=random.choice(a)
        a=a.pop(b)
    return b
suiji(a)
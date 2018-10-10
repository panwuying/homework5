'''class panduan:
    def __init__(self,str1):
        self.str1=str1
    def panduan1(self):
        sum=0
        for i in self.str1:
            if '-'==i:
                sum+=1
        if(len(self.str1)==11 and self.str1[3]=='-' and self.str1[6]=='-' and sum==2):
            b=self.str1
            c=b.replace('-','')
            if c.isdigit()==True:
                print'vaild ssn'
            else:
                print'invalid ssn'
        else:
            print'invalid ssn'
a=raw_input(">>")
panduan(a).panduan1()'''
'''def str(a,b):
    print a.find(b)
a=raw_input(">>")
b=raw_input(">>")
str(a,b)'''
'''a=raw_input(">>")
q=0
if len(a)>=8 and a.isalnum()==True:
    for i in a:
        if i.isdigit()==True:
            q+=1
        if q==2:
            print("vaildssn")
            break
    if q<2:
        print("in ssn")
else:
    print("in ssn")
'''
class you:
    def __init__(self,a):
        self.a=a
    def countletters(self):
        q=0
        if len(a)>0:
            for i in a:
                if i.islower()==True or i.isupper()==True:
                    q+=q
                if q>0:
                    print(q)
                else:
                    print(0)
         else:
             print(0)
a=raw_input(">>>")
you(a).countletters()
    



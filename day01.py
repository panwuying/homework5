'''class rectangle:
    def __init__(self,a=1,b=2):
        self.a=a
        self.b=b
    def getarea(self):
        print(self.a*self.b)
    def getperimeter(self):
        print((self.a+self.b)*2)
p=rectangle(4,40)
p.getarea()
p.getperimeter()
q=rectangle(3.5,35.7)
q.getarea()
q.getperimeter()
class account:
    def __init__(self,id=0,balance=100,rate=0):
        self.__id=int(id)
        self.__balance=float(balance)
      ''' ''' self.__rate=float(rate)
    def getmonthlyinterestrate(self):
        #print(self.__rate/100/12)
         return self.__rate/100/12
    def getmonthlyinterest(self):
        return self.__balance*self.getmonthlyinterestrate()
    def withdrw(self,a1):
        self.a1=a1
        self.__balance=self.__balance-a1
    def deposit(self,a2):
        self.a2=a2
        self.__balance=self.__balance+a2
    def print1(self):
        print(self.__id,self.__balance,self.getmonthlyinterestrate()*100,self.getmonthlyinterest())
a11=account(1122,20000,4.5)
a11.print1()
a11.withdrw(2500)
a11.print1()
a11.deposit(3000)
a11.print1()''''''
import math
class regularpolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=int(n)
        self.__side=float(side)
        self.__x=float(x)
        self.__y=float(y)
    def getperimeter(self):
        print(self.__n*self.__side)
    def getarea(self):
        print((self.__n*self.__side*self.__side)/(4*math.tan(math.pi/self.__n)))
regularpolygon().getperimeter()
regularpolygon().getarea()
regularpolygon(6,4).getperimeter()
regularpolygon(6,4).getarea
regularpolygon(10,4,5,6,7,8).getperimeter()
regularpolygon(10,4,5,6,7,8).getarea()'''




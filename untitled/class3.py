class A:
    a=10
    b=20
    def __init__(self,b,c):
        self.b=b
        self.c=c

    def disp(self,name):
        print("Name is ",name)
        print("value stored in object",self)
        print(self.a,self.b,self.c)
    def add(self):
        return self.a+self.b+self.c

obj=A(25,35)
A.disp(obj,'Kishan')
sum = A.add(obj)
print(sum)
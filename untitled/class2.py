class A:
    a=10
    b=20
    def __init__(self):
        self.c=25
        print('contents of self',self)
        print("Constructor is invoked")
class B:
    a=30
    b=40
    def __init__(self,c):
        self.c=c
        print('contents of self',self)
        print("Constructor is invoked")
print('non Parameterized constructor is created')
obj =A()
print("Parameterized constructor is created")
obj1 = B(55)
print("Address inside the object",obj)
print(obj.a,obj.b,obj.c)
print(A.a,A.b) #variables which are declared in init function are only accessed by obj not by Class
print(obj1.a,obj1.b,obj1.c)
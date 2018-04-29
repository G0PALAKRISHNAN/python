a={}
print("a =",type(a))
a={'a':'Apple','b':'Ball','c':'Cat','d':'Dog'}
print("a =",a)
print("a['b'] =",a['b'])
a['b']={'Ball','Bat','Bag'}
print("a =",a)
a['b']={'Bat':'Cricket','Ball':'Volleyball'}
print("a =",a)
print("a['b']['Bat'] =",a['b']['Bat'])
print("\nOperations on Dictionaries")
print("1.Length")
print("Length of dictionary variable a =",len(a))
print("Length of dictionary a['b'] =",len(a['b']))
print("\n2. Copy")
b=a.copy()
print("b =",b)
b.pop('b')
print("a =",a)
print("b =",b)

for i in a.values():
    print(i)
a= tuple() #creating empty tuple
print("a =",a)
b=(1,2,3,4,5,6,2,8,2,6)  #creating a tuple
print("b =",b)
c =()
d= 1,2,3,4,5
print("Type of variable c :",type(c))
print("Type of variable d :",type(d),d)
print("\nOperations on Tuple")
print("1. Count")
print("No. of elements in the Tuple b :",b.count(2))  #count(value)
print("\n2. Index")
print("b.index(2) =",b.index(2))
print("b.index(6,3,7) =",b.index(6,3,7))
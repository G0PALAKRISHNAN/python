a=set()
a={1,2,3,7,8,6,5,9,4}
print("Type of variable a :",type(a))
print("a =",a)
print("\nOperations on Sets")
print("1. Add")
a.add(6)
print("a.add(6) =",a)  #the set will not take the duplicate value
a.add(11)
print("a.add(11) =",a)
print("\n2. Copy")
b=a.copy()
print("b=a.copy() =",b)
print("\n3. Clear")
b.clear()
print("b.clear() =",b)
print("\n4. Union")
a={1,2,3,4,5}
b={4,5,6,7,8}
print("a =",a)
print("b =",b)
print("a.union(b) =",a.union(b))
print('\n5.Intersection')
print("a.intersection(b) =",a.intersection(b))
print('\n6. issubset')
c={1,2,3}
print("c.issubset(a) =",c.issubset(a))
print("c.issubset(b) =",c.issubset(b))
print('\n7. isdisjoint')
a={1,2,3,4}
b={5,6,7,8}
print("a.isdisjoint(b) =",a.isdisjoint(b))
print("c.isdisjoint(a) =",c.isdisjoint(a))
print('\n8. isssuperset')
a={1,2,3,4,5,6}
print("a.issuperset(c) =",a.issuperset(c))
print("c.issuperset(a) =",c.issuperset(a))
print("\n9. Pop")
print("a =",a)
a.pop()
print("a.pop() =",a)   #very first element in the set will get deleted
print("\n 10.Remove")
a={1,2,3,4,5,6}
print("a =",a)
a.remove(4)  #user defined deletion
print("a.remove() =",a)
print("\n11. Difference")
a={1,2,3,4,5,6}
b={5,6,7,8,9}
print("a.difference(b) =",a.difference(b))  #a-b
print("b.difference(a) =",b.difference(a))  #b-a
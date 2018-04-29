a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print("a[", i, "] =", a[i], "  a[", -i - 1, "] =", a[-i - 1])
print("a[-2] =", a[-2])

print("a[2:4] =", a[2:4])
print("-----Operations on List variables-----")
print("1. Appending")
print('a =', a)
a.append(6)
print("a =", a)

print("\n2. Copy")
print("2.1 Shallow copy")
b = a.copy()
print("b =", b)
b.append(2)
print("After appending")
print("b =", b)
print("\n2.2 Deep copy")
c = a
print("c =", c)
c.append("dinga")
print("After appending")
print('a =', a)
print('c =', c)

print('\n3. Count')
print("b.count() =",b.count(2))

print("\n4. Extend")
b.extend("HELLO")
print("b =",b)

print("\n5. Index")
print("b.index('E') =",b.index('E'))
print("b.index(2,5) =",b.index(2,5))
b.append(2)
print("b =",b)
print("b.index(2,7) =",b.index(2,7))
print("b.index('L',6,12) =",b.index('L',6,12))  #index(value, start_index, End _index)

print("\n6.Pop")
b.pop()
print("b =",b)
for i in range(5):
    b.pop()
print("b =",b)

print("\n7. Insert")
b.insert(4,"Dinga") #insert(position, value)
print("b =",b)

print("\n8. Remove")
b.remove(2)  #remove(value) removes first occurance of value
print('b =',b)

print("\n9. Reverse")
b.reverse()
print('b =',b)

print("\n10. Clear")
b.clear()
print("b =",b)

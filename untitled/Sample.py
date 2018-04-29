# a="hello world"
# print(a.capitalize())
# print(a.title())
# print(a.upper())
# print(a.lower())
# print(a.isalnum())
# print(a.count('l'))

a= [1,2,3,4,5,3,6,7]
a.append(8)
b=a #shallow copy : copies the value in the var:'a'
print(b)
# b.clear()
# print(b)
# print(a)
# print(a.count(3))
a.extend('String')
print(a.index(3,3))
print(a)
a.pop()
print(a)
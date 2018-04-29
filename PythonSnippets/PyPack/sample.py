# a = ["one","Five","Three"]
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum)
#
# avg = sum / len(a)
# print(avg)

# b=[1,3,2]
#
# c= a + b
# c.sort()
# print(c)
# length =0
# for i in a:
#     length[i] = len(i)
#     if length[i] > length[i+1] and length[i] > length[i+2]:
#         print(i)

text = input("enter the string")
text = text.lower()
word = text[::-1]
if text == word:
    print(word," Given text is palindrome")
else:
    print(word," Given text is not palindrome")

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)




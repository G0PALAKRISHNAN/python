class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word = word.lower()
        print(word.title())
        pal = word[::-1]
        print("After reversing the string")
        print(pal.title())
        if word == pal:
            return True
        else:
            return False

print("The given Word is Palindrome :",Palindrome.is_palindrome('Deleveled'))
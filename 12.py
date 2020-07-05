# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.


def is_palindrome(str):
    if ''.join(reversed(str)) == str:
        return True
    else:
        return False


str = input('enter a word')
print(is_palindrome(str))
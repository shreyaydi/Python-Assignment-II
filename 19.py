# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
class Validity:
    def is_valid(self, str):
        stack, pchar =[], {"(": ")", "{": "}", "[": "]"}
        for paranthese in str:
            if paranthese in pchar:
                stack.append(paranthese)
            elif len(stack) == 0 or pchar[stack.pop()] != paranthese:
                return False
        return len(stack) == 0


print(Validity().is_valid('(){}[]'))
print(Validity().is_valid('(){}[{{]}'))



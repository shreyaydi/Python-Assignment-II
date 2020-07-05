# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


def calculator(num1,num2, operator):
    if operator == '+':
        return num1+num2
    if operator == '-':
        return num1-num2
    if operator == '*':
        return num1*num2
    if operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return None

    else:
        return 'invalid operator'


n1 = float(input('enter first number'))
n2 = float(input('enter second number'))
op = input('enter the operator (+, -, *, /)')
print(calculator(n1,n2,op))

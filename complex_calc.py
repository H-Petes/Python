
num1 = float(input('ENTER FIRST NUMBER: '))
op = input('ENTER OPERATOR: ')
num2 = float(input('ENTER SECOND NUMBER: '))
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1/num2)
elif op == '%':
    print(num1 % num2)
else:
    print('SYNTAX ERROR')
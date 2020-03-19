try:
    
     10/0
     number = (int(input('ENTER NUMBER: ')))
     print(number)

except(ZeroDivisionError):
    print('SYNTAX ERROR')

except(ValueError):
      print('SYNTAX ERROR')
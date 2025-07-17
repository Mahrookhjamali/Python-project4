def add(x,y):
    return x+y
def substract(x,y):
    return x-y 
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
num1=float(input("Enter first number="))
num2=float(input("Enter second number="))
operation=input("Choose operation(+,-,*,/):")
if operation=='+':
    print(add(num1,num2))
elif operation=='-':
    print(substract(num1,num2))
elif operation=='*':
    print(multiplication(num1,num2))
elif operation=='/':
    print(division(num1,num2))
else:
    print("invalid input")

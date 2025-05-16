# simple calculator using match case statement

num1=input("Enter first number: ")
num2=input("Enter second number: ")
operation=input("Enter operation (+,-,*,/,%,^) : ")
match operation:
    case '+':
        result=float(num1)+float(num2)
        print(f"{num1} + {num2} = {result}")
    case '-':
        result=float(num1)-float(num2)
        print(f"{num1}-{num2} = {result}")
    case '*':
        result=float(num1)*float(num2)
        print(f"{num1}*{num2} = {result}")
    case '/':
        result=float(num1)/float(num2)
        print(f"{num1}/{num2} = {result}")
    case '%':
        result=float(num1)%float(num2)
        print(f"{num1}%{num2} = {result}")
    case '^':
        result=float(num1)**float(num2)
        print(f"{num1}^{num2} = {result}")
    case _:
        print("Invalid operation")

    

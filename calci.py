while True:
    try:
        op1 = int(input("Enter the first operand: "))
        op2 = int(input("Enter the second operand: "))
    except ValueError:
        print("Please enter valid integers.")
        continue
    
    while True:
        op = input("Enter an operator (+, -, *, /, %, ^): ")
        if op in ['+', '-', '*', '/', '%', '^']:
            break
        else:
            print("Invalid operator! Please enter a valid operator.")
            continue
    
    if op == '+':
        res = op1 + op2
    elif op == '-':
        res = op1 - op2
    elif op == '*':
        res = op1 * op2
    elif op == '/':
        if op2 == 0:
            print('Zero division error. Second operand cannot be zero.')
            continue
        else:
            res = op1 / op2
    elif op == '%':
        res = op1 % op2
    elif op == '^':
        res = op1 ** op2
  
    print(f'\n {op1} {op} {op2} = {res}')
    
    rep = input("Do you want to calculate more? ('y' for yes and 'n' for No): ").lower()
    print('\n')
    if rep == 'y':
        continue
    else:
       break

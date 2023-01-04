# --| 1 |-- #
def calcule(num01: int, operator: str, num02: int):
    match operator:
        case '+':
            return num01 + num02
        case '-':
            return num01 - num02
        case '*':
            return num01 * num02
        case '/':
            return num01 / num02
        case '%':
            return num01 % num02
        case _:
            return 'Incorrect value'


print(f'\nFirst method :')
print(calcule(4, '+', 5))  # 9
print(calcule(4, '-', 5))  # -1
print(calcule(4, '*', 5))  # 20
print(calcule(4, '/', 5))  # 0.8
print(calcule(4, '%', 5))  # 4
print(calcule(4, 'b', 5))  # Incorrect value


# --| 2 |-- #
def calcule_if(num01_if: int, operator_if: str, num02_if: int):
    if operator_if == '+':
        return num01_if + num02_if
    elif operator_if == '-':
        return num01_if - num02_if
    elif operator_if == '*':
        return num01_if * num02_if
    elif operator_if == '/':
        return num01_if / num02_if
    elif operator_if == '%':
        return num01_if % num02_if
    else:
        return 'Incorrect value'


print(f'\nSecond method :')
print(calcule_if(4, '+', 5))  # 9
print(calcule_if(4, '-', 5))  # -1
print(calcule_if(4, '*', 5))  # 20
print(calcule_if(4, '/', 5))  # 0.8
print(calcule_if(4, '%', 5))  # 4
print(calcule(4, 'b', 5))  # Incorrect value

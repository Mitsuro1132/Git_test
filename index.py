def plus(a,b):
    return a + b

def negative(a,b):
    return a - b

def mnojenya(a,b):
    return a * b

def dilenya(a,b):
    if b == 0:
        return "Ділити на 0 неможна "
    else:
        return a / b


operation = input("Введіть операцію калькулятора (+,-,*,/)")

num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))



if operation == "+":
    print(plus(num_1,num_2))
elif operation == "-":
    print(negative(num_1,num_2))
elif operation == "*":
    print(mnojenya(num_1,num_2))
elif operation == "/":
    print(dilenya(num_1,num_2))
    
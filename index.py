def plus(a,b):
    return a + b

def negative(a,b):
    return a - b

operation = input("Введіть операцію калькулятора (+,-,*,/)")

num_1 = input("Введіть перше число: ")
num_2 = input("Введіть друге число: ")

if operation == "+":
    print(plus(num_1,num_2))
elif operation == "-":
    print(negative(num_1,num_2))
grades = []

def add_grade(grade):
    grades.append(grade)

def show_grade():
    print(f"Grade: {grades}")

def max_grade():
    return max(grades)

def min_grade():
    return min(grades)

def ser_grade():
    return sum(grades)/len(grades)


while True:
    print("1 - Додати оцінку")
    print("2 - Показати оцінки")
    print("3 - Показати максимальну")
    print("4 - Показати мінімальну")
    print("5 - Показати середнє")
    print("0 - Вихід")

    num_input = int(input("Оберіть дію "))

    if num_input == 1:
        num_grade = int(input("Введіть оцінку "))
        add_grade(num_grade)

    elif num_input == 2:
        show_grade()

    elif num_input == 3:
        print(max_grade())

    elif num_input == 4:
        print(min_grade())

    elif num_input == 5:
        print(ser_grade()) 

    elif num_input == 0:
        print("Програма завершена")
        break

    else:
        print("Невірний вибір")

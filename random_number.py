import random as rand

secret_number = rand.randint(1,100)

while True:
    input_number = int(input("Спробуйте вгадати число (1-100): "))

    if input_number > secret_number:
        print("Спробуй меньше!")

    elif input_number < secret_number:
        print("Спробуй більше!")

    elif input_number == secret_number:
        print("Ви вгадали!")
        break   
import random

while True:
    number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Угадай число от 1 до 10: "))
            if 1 <= guess <= 10:
                break
            else:
                print("Пожалуйста, введите число от 1 до 10.")
        except ValueError:
            print("Некорректный ввод. Введите, пожалуйста, целое число.")

    if guess == number:
        print("Поздравляю! Вы угадали число.")
    else:
        print("К сожалению, вы не угадали. Загаданное число было:", number)

    restart = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
    if restart == "нет":
        print("Спасибо за игру! До свидания!")
        break
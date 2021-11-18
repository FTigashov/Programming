import random

def play():
    a = random.randint(0, 5)
    n = 7
    print("Игра угадай число ")
    while (n != a):
        n = int(input("Введите число от 0 до 5: "))
        if (n < 0 or n > 5):
            print("Число не входит в диапазон")
        else:
            if n == a:
                print("Угадали!")
            elif (a < n):
                print("Заданное число меньше")
            else:
                print("Загаданное число больше")




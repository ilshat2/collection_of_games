import random

lowDigit = 10      # Нижняя граница случайного числа
highDigit = 50     # Верхняя граница случайного числа
digit = 0          # Загаданное компьбтером число

countInput = 0     # Количество попыток угадать
win = False        # Угадал текущее чило?
playGame = True    # Продолжвется ли игра?
x = 0              # Число которое вводит пользователь
startScore = 100   # Начальное количество очков
score = 0          # Текущее количестно очков
maxScore = 0       # Максимальное кольчесвто очков за игру


while (playGame):
    digit = random.randint(lowDigit, highDigit)
    print('Компьютер загадал число, попробуйте отгадать!\n')
    print(f'Компьютер загадал {digit}\n')  # Строка для проверки

    # Внутренний цикл
    while (not win):
        x = ''
        while (not x.isdigit()):
            x = input(f'Введите число от {lowDigit} до {highDigit}:\n')
            print(int(x) < lowDigit)
            if x.isdigit() and ((int(x) < lowDigit) or (int(x) > highDigit)):
                print(f'Числа должны быть в диапозоне от {lowDigit} до {highDigit}:\n')
            elif x.isdigit() != digit:
                print('Вы не угадали(\n')
            elif (not x.isdigit()):
                print('.' * 27 + 'Введите, пожалуйства, число.\n')

        x = int(x)

        if (x == digit):
            print('Победа!!!')
            # Сбрасываем win
            win = True
    if (input('Enter - сыграть снова, 0 - выход') == '0'):
        playGame = False
    else:
        win = False

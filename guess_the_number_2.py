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


digit = random.randint(lowDigit, highDigit)
print('Компьютер загадал число, попробуйте отгадать!')
print(f'Компьютер загадал {digit}')  # Строка для проверки

x = ''
while (not x.isdigit()):
    x = input(f'Введите число от {lowDigit} до {highDigit}: ')
    if (not x.isdigit()):
        print('.' * 27 + 'Введите, пожалуйства, число.')

x = int(x)

if (x == digit):
    print('Победа!!!')

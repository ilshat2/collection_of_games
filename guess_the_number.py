import random


def check_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Ошибка: введите корректное число!")


print('-' * 70)
print('Это игра где Компьютер загадал число от 1 до 20 вам нужно его отгадать.')
print('-' * 70)

user_answer = 1  # Решение пользователя о том стоит ли продолжать

victory = 0  # Счетчик побед
defeat = 0   # Счетчик поражений
while user_answer > 0:
    hidden_number = random.randint(1, 20)  # Случайное число от 1 до 20
    print(f'комп загадал {hidden_number}')
    while user_answer != hidden_number:
        print('Загадайте число от 1 до 20')
        user_number = check_number(int(input()))  # Число загаданное пользователем
        if user_number == hidden_number:
            print('Вы победили!!!')
            victory += 1
            break
        else:
            defeat += 1
            print('Вы не угадали(')
    print(f'Побед = {victory}')
    print(f'Поражений = {defeat}')
    print('Enter - сыграть снова, 0 - выход')
    user_answer = int(input())  # Решение пользователя о том стоит ли продолжать
print('Спасибо за игру!')


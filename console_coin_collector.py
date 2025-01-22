import random


# Создание игрового поля и персонажа
field_size = 10
player_x = 0
player_y = 0  # Начальная позиция персонажа


def draw_field():
    for y in range(field_size):
        for x in range(field_size):
            if x == player_x and y == player_y:
                print('@', end=' ')  # Персонаж
            else:
                print('.', end=' ')  # Пустое поле
        print()
    print()


draw_field()


# Добавляем движение персонажа
def move_player(direction):
    global player_x, player_y
    if direction == 'w' and player_y > 0:
        player_y -= 1
    elif direction == 's' and player_y < field_size - 1:
        player_y += 1
    elif direction == 'a' and player_x > 0:
        player_x -= 1
    elif direction == 'd' and player_x < field_size - 1:
        player_x += 1


while True:
    draw_field()
    command = input("Введите направление (W/A/S/D): ").lower()
    move_player(command)


# Генерация монеты
coin_x, coin_y = random.randint(0, field_size - 1), random.randint(0, field_size - 1)


def draw_field():
    for y in range(field_size):
        for x in range(field_size):
            if x == player_x and y == player_y:
                print('@', end=' ')
            elif x == coin_x and y == coin_y:
                print('$', end=' ')  # Монета
            else:
                print('.', end=' ')
        print()
    print()


# Счётчик очков
score = 0


def check_coin():
    global score, coin_x, coin_y
    if player_x == coin_x and player_y == coin_y:
        score += 1
        print(f"Монета собрана! Очки: {score}")
        coin_x, coin_y = random.randint(0, field_size - 1), random.randint(0, field_size - 1)


while True:
    draw_field()
    command = input("Введите направление (W/A/S/D): ").lower()
    move_player(command)
    check_coin()


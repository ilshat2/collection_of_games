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

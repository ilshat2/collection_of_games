import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])

def player_move(board):
    while True:
        try:
            move = int(input("Выберите позицию (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Эта клетка уже занята.")
        except (ValueError, IndexError):
            print("Неверный ввод. Попробуйте снова.")

def computer_move(board):
    print("Ход компьютера...")
    while True:
        move = random.randint(0, 8)
        row, col = divmod(move, 3)
        if board[row][col] == " ":
            board[row][col] = "O"
            break

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if check_win(board, "X"):
            print("Вы выиграли!")
            break
        if check_draw(board):
            print("Ничья!")
            break
        computer_move(board)
        print_board(board)
        if check_win(board, "O"):
            print("Компьютер выиграл!")
            break
        if check_draw(board):
            print("Ничья!")
            break

if __name__ == "__main__":
    play_game()

# - Пустая ячейка
# X Крестик
# O Нолик

from random import randint


def draw_board(Current_list):
    if len(Current_list) != 9:
        return '!!!ERROR 003: Не верный draw_list!!!'
    for i in range(0, 9, 3):
        print(Current_list[i], Current_list[i + 1], Current_list[i + 2])
    print()


def get_player_move(Current_list, Ms):
    while True:
        X = int(input('Введи координату X (От 1 до 3) '))
        Y = int(input('Введи координату Y (От 1 до 3) '))
        move = X + 3 * (Y - 1) if Y > 1 else X
        if X not in {1, 2, 3} or Y not in {1, 2, 3}:
            print('!!!ERROR 001: Вне диапазона!!!')
            continue
        if Current_list[move - 1] in ['X', 'O']:
            print('!!!ERROR 002: Точка уже занята!!!')
            continue
        Current_list[move - 1] = Ms
        return Current_list


def get_computer_move(Current_list, Ms):
    possible_moves = []
    for i in range(0, 8):
        if Current_list[i] == '-':
            possible_moves.append(i)
    move = randint(0, len(possible_moves))
    Current_list[possible_moves[move - 1]] = Ms
    return Current_list


def check_win(Current_list, Ms):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(Current_list[i] == Current_list[j] == Current_list[k] == Ms for i, j, k in win_conditions)


if __name__ == '__main__':
    Current_pos = ['-' for i in range(9)]
    PMs = 'X' if randint(1, 2) == 1 else 'O'
    CMs, PlMs = 'X', PMs
    print('Первым ходишь ты' if PMs == "X" else 'Первым ходит компьютер')
    while '-' in Current_pos:
        get_computer_move(Current_pos, CMs) if PMs == 'O' else get_player_move(Current_pos, CMs)
        if check_win(Current_pos, CMs) is True:
            draw_board(Current_pos)
            print("Ты Победил!" if CMs == PlMs else "Ты Проиграл :(")
            break
        draw_board(Current_pos)
        CMs, PMs = 'O' if CMs == 'X' else 'X', 'O' if PMs == 'X' else 'X'
    else:
        print('Ничья, Поле закончилось :|')

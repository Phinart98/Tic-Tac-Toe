board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

print("---------")
print(f"| {board[0]} {board[1]} {board[2]} |")
print(f"| {board[3]} {board[4]} {board[5]} |")
print(f"| {board[6]} {board[7]} {board[8]} |")
print("---------")

possible_spots = {"1 3": 0, "1 2": 3, "1 1": 6,
           "2 3": 1, "2 2": 4, "2 1": 7,
           "3 3": 2, "3 2": 5, "3 1": 8}

turn = 'X'

while True:
    user_input = input("Enter the coordinates as pertaining to a cartesian plain: ")
    coordibates = user_input.split()
    if coordibates[0].isdigit() is False or coordibates[1].isdigit() is False:
        print("You should enter numbers separated by a space!")
        continue
    elif 1 < int(coordibates[0]) > 3 or 1 < int(coordibates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif board[possible_spots[user_input]] != '_':
        print("This cell/coordinate is occupied! Choose another one!")
        continue
    else:
        board[possible_spots[user_input]] = turn

    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'

    print('---------')
    print(f'| {board[0]} {board[1]} {board[2]} |')
    print(f'| {board[3]} {board[4]} {board[5]} |')
    print(f'| {board[6]} {board[7]} {board[8]} |')
    print('---------')

    rows = []
    columns = [[board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]]]
    backslash_pattern = [[board[0], board[4], board[8]]]
    forward_slash_pattern = [[board[2], board[4], board[6]]]

    O_wins = ['O', 'O', 'O']
    X_wins = ['X', 'X', 'X']

    single_row = []
    for letter in board:
        single_row.append(letter)
        if len(single_row) == 3:
            rows.append(single_row)
            single_row = []

    total = rows + columns + backslash_pattern + forward_slash_pattern

    O_true = O_wins in total
    X_true = X_wins in total

    if O_true and X_true or abs(board.count('O') - board.count('X')) >= 2:
        print('Impossible')
        break
    elif O_true:
        print('O wins')
        break
    elif X_true:
        print('X wins')
        break
    elif board.count('_') == 0:
        print('Draw')
        break

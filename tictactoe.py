user_input = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
user_list = user_input
game_finished = 0


def print_game():
    print('---------')
    print('| ' + user_input[0] + ' ' + user_input[1] + ' ' + user_input[2] + ' |')
    print('| ' + user_input[3] + ' ' + user_input[4] + ' ' + user_input[5] + ' |')
    print('| ' + user_input[6] + ' ' + user_input[7] + ' ' + user_input[8] + ' |')
    print('---------')


print_game()
global grid, coords


def check_input():
    global grid, coords
    grid = input('Enter the coordinates: ')
    coords = grid.split(' ')
    # check if input is numeric
    if not coords[0].isdigit() or not coords[1].isdigit():
        print('You should enter numbers!')
        check_input()
    # check if input is in range
    elif (int(coords[0]) > 3) or (int(coords[0]) < 1) or (int(coords[1]) > 3) or (int(coords[1]) < 1):
        print('Coordinates should be from 1 to 3!')
        check_input()


def evaluate_o():
    check_input()
    global grid, user_list, user_input
    if grid == '1 1' and user_input[0] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '1 1' and user_input[0] == '_':
        user_list[0] = 'O'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '1 2' and user_input[1] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '1 2' and user_input[1] == '_':
        user_list[1] = 'O'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '1 3' and user_input[2] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '1 3' and user_input[2] == '_':
        user_list[2] = 'O'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '2 1' and user_input[3] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '2 1' and user_input[3] == '_':
        user_list[3] = 'O'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '2 2' and user_input[4] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '2 2' and user_input[4] == '_':
        user_list[4] = 'O'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '2 3' and user_input[5] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '2 3' and user_input[5] == '_':
        user_list[5] = 'O'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '3 1' and user_input[6] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '3 1' and user_input[6] == '_':
        user_list[6] = 'O'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '3 2' and user_input[7] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '3 2' and user_input[7] == '_':
        user_list[7] = 'O'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '3 3' and user_input[8] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_o()
    elif grid == '3 3' and user_input[8] == '_':
        user_list[8] = 'O'
        user_input = ''.join(user_list)
        print_game()


def evaluate_x():
    check_input()
    global grid, user_list, user_input
    if grid == '1 1' and user_input[0] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '1 1' and user_input[0] == '_':
        user_list[0] = 'X'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '1 2' and user_input[1] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '1 2' and user_input[1] == '_':
        user_list[1] = 'X'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '1 3' and user_input[2] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '1 3' and user_input[2] == '_':
        user_list[2] = 'X'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '2 1' and user_input[3] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '2 1' and user_input[3] == '_':
        user_list[3] = 'X'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '2 2' and user_input[4] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '2 2' and user_input[4] == '_':
        user_list[4] = 'X'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '2 3' and user_input[5] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '2 3' and user_input[5] == '_':
        user_list[5] = 'X'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '3 1' and user_input[6] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '3 1' and user_input[6] == '_':
        user_list[6] = 'X'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '3 2' and user_input[7] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '3 2' and user_input[7] == '_':
        user_list[7] = 'X'
        user_input = ''.join(user_list)
        print_game()
    elif grid == '3 3' and user_input[8] != '_':
        print('This cell is occupied! Choose another one!')
        evaluate_x()
    elif grid == '3 3' and user_input[8] == '_':
        user_list[8] = 'X'
        user_input = ''.join(user_list)
        print_game()


def evaluate_results():
    row_1 = user_input[0] + user_input[1] + user_input[2]
    row_2 = user_input[3] + user_input[4] + user_input[5]
    row_3 = user_input[6] + user_input[7] + user_input[8]
    col_1 = user_input[0] + user_input[3] + user_input[6]
    col_2 = user_input[1] + user_input[4] + user_input[7]
    col_3 = user_input[2] + user_input[5] + user_input[8]
    dia_1 = user_input[0] + user_input[4] + user_input[8]
    dia_2 = user_input[6] + user_input[4] + user_input[2]
    lines = [row_1, row_2, row_3, col_1, col_2, col_3, dia_1, dia_2]
    x_counter = 0
    o_counter = 0
    _counter = 0
    global game_finished
    for x in row_1:
        if x == 'X':
            x_counter += 1
    for x in row_2:
        if x == 'X':
            x_counter += 1
    for x in row_3:
        if x == 'X':
            x_counter += 1
    for o in row_1:
        if o == 'O':
            o_counter += 1
    for o in row_2:
        if o == 'O':
            o_counter += 1
    for o in row_3:
        if o == 'O':
            o_counter += 1
    for y in row_1:
        if y == '_':
            _counter += 1
    for y in row_2:
        if y == '_':
            _counter += 1
    for y in row_3:
        if y == '_':
            _counter += 1
    if x_counter - o_counter >= 2:
        print('Impossible')
        
    elif o_counter - x_counter >= 2:
        print('Impossible')
        exit()
    elif 'XXX' in lines and 'OOO' in lines:
        print('Impossible')
        exit()
    elif 'XXX' in lines:
        print('X wins')
        exit()
    elif 'OOO' in lines:
        print('O wins')
        exit()
    elif 'OOO' not in lines and 'XXX' not in lines and _counter == 0:
        print('Draw')
        exit()


while True:
    evaluate_x()
    evaluate_results()
    evaluate_o()
    evaluate_results()

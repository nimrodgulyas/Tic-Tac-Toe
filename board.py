tabla = ['.', ".", ".",
        '.', ".", ".",
        '.', ".", "."]
def get_empty_board():
    for elem in tabla:
        if elem == ".":
            sublist1 = tabla[0:3]
            sublist2 = tabla[3:6]
            sublist3 = tabla[6:9]
            return [sublist1, sublist2, sublist3]

board = get_empty_board()
def display_board(board):
    print("    1    2    3")
    print("A",  board[0])
    print("B",  board[1])
    print("C",   board[2])
print(display_board(board))

def is_board_full(board):
    for i in board:
        if i == '.':
            return True
        else:
            return False


def get_winning_player(board):
    x  = 0
    O = 0
    if board[0] == ['X', 'X', 'X'] or board[1] == ['X', 'X', 'X'] or board[2] == ['X', 'X', 'X'] or board[0][0] == 'X' and board[1][0] == 'X' and board [2][0] == 'X' or board[0][1] == 'X' and board[1][1] == 'X' and board [2][1] == 'X' or board[0][2] == 'X' and board[1][2] == 'X' and board [2][2] == 'X' or board[0][0] == 'X' and board[1][1] == 'X' and board [2][2] == 'X' or board[0][2] == 'X' and board[1][1] == 'X' and board [2][0] == 'X':
        x += 1
        return x
    elif board[0] == ['O', 'O', 'O'] or board[1] == ['O', 'O', 'O'] or board[2] == ['O', 'O', 'O'] or board[0][0] == 'O' and board[1][0] == 'O' and board [2][0] == 'O' or board[0][1] == 'O' and board[1][1] == 'O' and board [2][1] == 'O' or board[0][2] == 'O' and board[1][2] == 'O' and board [2][2] == 'O' or board[0][0] == 'O' and board[1][1] == 'O' and board [2][2] == 'O' or board[0][2] == 'O' and board[1][1] == 'O' and board [2][0] == 'O':
        O += 2
        return O
    return True


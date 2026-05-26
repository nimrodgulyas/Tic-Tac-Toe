def get_empty_board():
    return [['.', '.', '.'], 
            ['.', '.', '.'], 
            ['.', '.', '.']]

def display_board(board):
    print("   1   2   3")
    print(f"A  {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("  ---+---+---")
    print(f"B  {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("  ---+---+---")
    print(f"C  {board[2][0]} | {board[2][1]} | {board[2][2]}")

def is_board_full(board):
    for sor in board:
        for elem in sor:
            if elem == '.':
                return False
    return True

def get_winning_player(board):
    #vízszint
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
            return board[i][0]
            
    #függőleges oszlopok 
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            return board[0][i]
            
    # átlók
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]
        
    return None

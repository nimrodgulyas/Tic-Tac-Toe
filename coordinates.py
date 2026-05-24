from board import get_winning_player
from board import is_board_full
import board

def get_human_coordinates(board):
    player = (input("Which player are you? X/O?: "))
    sor = (int(input("Which line do you want to put your symbol?(The first one is 0): ")))
    eleme = (int(input("On which index do you want your symbol to be?(The first one is 0): ")))
    while is_board_full != True:
        for i in board:
            if player == ("X"):
                board[sor][eleme] = "X"
            elif player == ("O"):
                board[sor][eleme] = "O"
            print(board)


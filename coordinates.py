from board import get_winning_player
import board

def get_human_coordinates(board):
    valasztas = (input("Which player are you? X/O?: "))
    sor = (int(input("Which line do you want to put your symbol?(The first one is 0): ")))
    eleme = (int(input("On which index do you want your symbol to be?(The first one is 0): ")))
    while get_winning_player != True:
        for i in board:
            if valasztas == ("X"):
                board[sor][eleme] == "X"
            elif valasztas == ("O"):
                board[sor][eleme] == "O"
            print(board)
            
print(get_human_coordinates(board))
print(get_winning_player)
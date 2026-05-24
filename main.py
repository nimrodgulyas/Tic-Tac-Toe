from board import get_winning_player
from coordinates import get_human_coordinates
from menu import get_menu_option
from board import get_empty_board
from board import display_board
from board import is_board_full
import board

print("Welcome to the Ti-Tac-Toe game!")
mod = get_menu_option()
if mod == 1:
    board = get_empty_board()
    current_player = 'X'
    

while is_board_full(board) == False:
    board = get_human_coordinates(board)
    winner = get_winning_player(board)
    
    if get_winning_player(board) == 'X':
        winner = 'X'
        break
    
    if get_winning_player(board) == 'O':
        winner = 'O'
        break
    
    print(f"Congratulates! The winner is {winner}!")
        
    if is_board_full() == True and winner != 'X' or winner != "O":
        print("It's a tie! The board is full!")
        break
    
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
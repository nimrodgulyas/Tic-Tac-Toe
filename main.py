from board import get_winning_player
from coordinates import get_human_coordinates
from menu import get_menu_option
from board import get_empty_board
from board import is_board_full
import board
from board import display_board

# print("Welcome to the Ti-Tac-Toe game!")
# mod = get_menu_option()
# if mod == 1:
#     board = get_empty_board()
#     current_player = 'X'
    

# while is_board_full(board) == False:
#     for sor in board:
#         for elem in sor:
#             board = get_human_coordinates(board)
#             winner = get_winning_player(board)
    
#             if get_winning_player(board) == 'X':
#                 winner = 'X'
#                 print(f"Congratulates! The winner is {winner}!")
#                 break
    
#             if get_winning_player(board) == 'O':
#                 winner = 'O'
#                 print(f"Congratulates! The winner is {winner}!")
#                 break
    
            
        
#             if is_board_full() == True and winner != 'X' or winner != "O":
#                 print("It's a tie! The board is full!")
#                 break
    
#    if current_player == 'X':
#        current_player = 'O'
#    else:
#        current_player = 'X'

def main():
    board = get_empty_board()
    current_player = 'X'
    
    # Szótár, amivel a játékos betű-beviteleit indexszé alakítjuk (A->0, B->1, C->2)
    row_mapping = {'A': 0, 'B': 1, 'C': 2}
    
    print("Üdvözöllek a Tic-Tac-Toe játékban!")
    
    while True:
        display_board(board)
        print(f"\n'{current_player}' játékos köre következik.")
        
        # Lépés bekérése (pl.: A1 vagy B3)
        move = input("Adj meg egy koordinátát (pl. A1): ").upper().strip()
        
    # Egyszerű input ellenőrzés
        if len(move) != 2 or move[0] not in row_mapping or move[1] not in ['1', '2', '3']:
            print("Hibás formátum! Kérlek használj A1, B2 formátumot.")
            continue
            
        row = row_mapping[move[0]]
        col = int(move[1]) - 1
        
        # Ellenőrizzük, hogy üres-e a hely
        if board[row][col] != '.':
            print("Ez a hely már foglalt! Válassz másikat.")
            continue
            
        # Lépés végrehajtása
        board[row][col] = current_player
        
        # Van nyertes?
        winner = get_winning_player(board)
        if winner:
            display_board(board)
            print(f"\nGratulálok! A játékot '{winner}' nyerte!")
            break
            
        # Betelt a tábla?
        if is_board_full(board):
            display_board(board)
            print("\nDöntetlen! A tábla megtelt.")
            break
            
        # Játékos váltása
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
from board import get_winning_player
from board import get_empty_board
from board import is_board_full
from board import display_board

def main():
    board = get_empty_board()
    current_player = 'X'
    
    # Szótár, amivel a játékos betű-beviteleit indexszé alakítjuk (A->0, B->1, C->2)
    row_mapping = {'A': 0, 'B': 1, 'C': 2}
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        display_board(board)
        print(f"\n'{current_player}' the player's round is the next.")
        
        # Lépés bekérése (pl.: A1 vagy B3)
        move = input("Give a coordinate (eg. A1): ").upper().strip()
        
    # Egyszerű input ellenőrzés
        if len(move) != 2 or move[0] not in row_mapping or move[1] not in ['1', '2', '3']:
            print("Wrong format! Please use A1, B2 format.")
            continue
            
        row = row_mapping[move[0]]
        col = int(move[1]) - 1
        
        # Ellenőrizzük, hogy üres-e a hely
        if board[row][col] != '.':
            print("This place is already taken! Please choose another one.")
            continue
            
        # Lépés végrehajtása
        board[row][col] = current_player
        
        # Van nyertes?
        winner = get_winning_player(board)
        if winner:
            display_board(board)
            print(f"\nCongrats! '{winner}' won the game!")
            break
            
        # Betelt a tábla?
        if is_board_full(board):
            display_board(board)
            print("\nIt's a tie! The table is full.")
            break
            
        # Játékos váltása
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
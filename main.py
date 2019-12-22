from board import Board

def main():
    print("Welcome to the numbers game")
    game_board = Board()
    game_board.print_board()
    game_board.print_square(1, 1)

main()
print("\n")
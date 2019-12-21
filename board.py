from square import Square 

class Board:
    def __init__(self):
        self.board_pattern = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 1, 1, 2, 1, 3, 1, 4, 1], [5, 1, 6, 1, 7, 1, 8, 0, 0]]
        self.board = []
        for i in range(len(self.board_pattern)):
            self.board.append([])
            for j in range(len(self.board_pattern[i])):
                s = Square(self.board_pattern[i][j])
                self.board[i].append(s)

    def print_board(self):
        for i in range(len(self.board_pattern)):
            print("\n")
            for j in range(len(self.board_pattern[i])):
               print(str(self.board[i][j].get_value()) + ' ', end='')
        print("\n")
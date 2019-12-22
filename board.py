from square import Square 

class Board:
    def __init__(self):
        self.board_pattern = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 1, 1, 2, 1, 3, 1, 4, 1], [5, 1, 6, 1, 7, 1, 8, 0, 0]]
        self.board = []
        for i in range(len(self.board_pattern)):
            self.board.append([])
            for j in range(len(self.board_pattern[i])):
                s = Square(self.board_pattern[i][j], j, i)
                self.board[i].append(s)
        for row in self.board:
            for square in row:
                self.update_neighbors(square) 

    def print_board(self):
        for i in range(len(self.board_pattern)):
            print("\n")
            for j in range(len(self.board_pattern[i])):
               print(str(self.board[i][j].get_value()) + ' ', end='')
        print("\n")

    def print_square(self, x, y):
        print("The value is: " + str(self.board[y][x].get_value))
        print(self.board[y][x].get_top_neighbor().get_value())
        print(self.board[y][x].get_bottom_neighbor().get_value())
        print(self.board[y][x].get_left_neighbor().get_value())
        print(self.board[y][x].get_right_neighbor().get_value())
    
    def update_neighbors(self, square):
        # Check top neighbor
        y = square.get_y()
        print(y)
        for i in range(y, 0):
            if(self.board[i][square.get_x()].get_value > 0):
                square.set_top_neighbor(self.board[i][square.get_x()])
                break
            square.set_top_neighbor(None)
        # Check bottom neighbor
        for i in range(y, len(self.board)):
            if(self.board[i][square.get_x()].get_value() > 0):
                square.set_bottom_neighbor(self.board[i][square.get_x()])
                break
            square.set_bottom_neighbor(None)

        x_count = square.get_x()
        y_count = square.get_y()
        # Check left neighbor
        while(True):
            if x_count == 0 and y_count > 0:
                x_count = 8
                y_count -= 1
            elif x_count == 0 and y_count == 0:
                square.set_left_neighbor(None)
            else:
                x_count -= 1
            if self.board[y_count][x_count].get_value() > 0:
                square.set_left_neighbor(self.board[y_count][x_count])
                break

        x_count = square.get_x()
        y_count = square.get_y()
        # Check right neighbor
        while(True):
            if x_count == 8 and y_count < len(self.board):
                x_count = 8
                y_count -= 1
            elif x_count == 0 and y_count == 0:
                square.set_left_neighbor(None)

            x_count -= 1
            if self.board[y_count][x_count].get_value() > 0:
                square.set_left_neighbor(self.board[y_count][x_count])
                break    


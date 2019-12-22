class Square:
    def __init__(self, value, x, y):
        self.value = value
        self.left_neighbor = None
        self.right_neighbor = None
        self.top_neighbor = None
        self.bottom_neighbor = None
        self.__x = x
        self.__y = y
    
    def set_value(self, value):
        self.value = value

    def get_value(self):
        return(self.value)

    def get_x(self):
        return(self.__x)

    def get_y(self):
        return(self.__y)
    
    def set_top_neighbor(self, neighbor):
        self.top_neighbor = neighbor
    
    def set_bottom_neighbor(self, neighbor):
        self.bottom_neighbor = neighbor
    
    def set_left_neighbor(self, neighbor):
        self.left_neighbor = neighbor
    
    def set_right_neighbor(self, neighbor):
        self.right_neighbor = neighbor

    def get_top_neighbor(self):
        return(self.top_neighbor)
    
    def get_bottom_neighbor(self):
        return(self.bottom_neighbor)
    
    def get_left_neighbor(self):
        return(self.left_neighbor)

    def get_right_neighbor(self):
        return(self.right_neighbor)

    
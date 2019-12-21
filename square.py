class Square:
    def __init__(self, value):
        self.value = value
        self.left_neighbor = None
        self.right_neighbor = None
        self.top_neighbor = None
        self.bottom_neighbor = None

    def update_neighbors(self):
        pass
    
    def get_value(self):
        return(self.value)
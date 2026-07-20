import numpy as np
import Boats

class Map:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.grid = np.zeros((self.x,self.y), dtype=int)

    def create_grid(self):
        
        for i in range(self.x):
            for j in range(self.y):
                self.grid[i][j] = 0
    


class Tabletop:
    # constructor
    def __init__(self, x: int, y: int):
        self.x = x + 1
        self.y = y + 1
        self.grid = np.zeros((self.x, self.y), dtype=str)
        
    # create the grid that will be used to display the game
    def create_grid(self):
        
        for i in range(self.x):
            for j in range(self.y):
                self.grid[i][j] = '~'
        self.grid[0][0] = ' '
        for i in range(1, self.x):
            self.grid[i][0] = str(i-1)
            self.grid[0][i] = str(i-1)
    
    # display the grid
    def display(self):
        for i in range(self.x):
            for j in range(self.y):
                print(self.grid[i][j], end=' ')
            print()
        
                


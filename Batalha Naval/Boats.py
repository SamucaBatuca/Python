import numpy as np

class boat:
    # constructor
    def __init__(self, size:int, seed: int, coordenates: int, direction: bool):
        self.size = size
        self.seed = seed
        self.coordenates = coordenates
        self.id = int                                       # the boat's indentification
        self.direction = direction                          # 0 for horizontal, 1 for vertical
        self.value = int                                      # the boat's number

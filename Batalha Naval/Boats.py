import numpy as np

class boat:
    # constructor
    def __init__(self, size:int, seed: int, coordenates: int, direction: bool):
        self.size = size
        self.seed = seed
        self.coordenates = coordenates
        self.damage = False
        self.direction = direction                          # 0 for horizontal, 1 for vertical
        self.value:int                                      # the boat's number

    def get_damage(self):
        self.damage = True


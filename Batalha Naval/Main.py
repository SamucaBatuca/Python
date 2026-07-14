import numpy as np
import Boats
import Game_map as Map
import random

list = []

def create_boats(quantity: int):
    for i in range(quantity):
        barco = Boats.boat(random.randint(1,3),seed=random.randint(0,9),coordenates=random.randint(0,9), direction=random.randint(0,1))
        barco.value = i+1
        list.append(barco)
        

def place_boat(barco: Boats.boat, mapa: Map.Map, time: int):



    if time >= 2:
        barco = Boats.boat(barco.size,seed=random.randint(0,9), direction=random.randint(0,1))
        return place_boat(barco, mapa, 0)
    
    # horizontal placement
    if barco.direction == 0:
        for i in range(barco.size):
            # try to place the boat in the right direction
            if barco.coordenates + i < mapa.x and mapa.grid[barco.seed][barco.coordenates + i] == 0 :
                mapa.grid[barco.seed][barco.coordenates + i] = barco.value
            # if fails, try to place the boat in the left direction
            elif barco.coordenates - (barco.size - i) >=0 and mapa.grid[barco.seed][barco.coordenates - i] == 0 :
                mapa.grid[barco.seed][barco.coordenates - (barco.size - i)] = barco.value
            # if fails, try to place the boat in the vertical
            else:
                # clean the map before and after the seed value
                for j in range(barco.size):
                    if barco.coordenates + i < mapa.x and mapa.grid[barco.seed][barco.coordenates + j] == barco.value:
                        mapa.grid[barco.seed][barco.coordenates + j] = 0
                    if barco.coordenates - (barco.size - i) >=0 and mapa.grid[barco.seed][barco.coordenates - j ] == barco.value:
                        mapa.grid[barco.seed][barco.coordenates - j] = 0
                barco.direction = not barco.direction
                return place_boat(barco, mapa, time + 1)




barco = Boats.boat(3,seed=random.randint(0,10),coordenates=random.randint(0,10), direction=0)
tabuleiro = Map.Tabletop(10,10)
mapa = Map.Map(10,10)
#barco = Boats.boat(2,2,10,0)
barco.value = 7
mapa.create_grid()

place_boat(barco,mapa,0)
print(barco.seed, barco.coordenates)
print(mapa.grid)
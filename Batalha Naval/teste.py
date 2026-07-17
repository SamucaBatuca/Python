import numpy as np
import Boats
import Game_map as Map
import random

boat_list = []

def create_boats(quantity: int):
    for i in range(quantity):
        barco = Boats.boat(i+4,seed=random.randint(0,9),coordenates=random.randint(0,9), direction=random.randint(0,1))
        barco.value = i+4
        boat_list.append(barco)
        

def place_boat(barco: Boats.boat, mapa: Map.Map, time: int):

    if time >= 2:
        aux = barco.value
        barco = Boats.boat(size=barco.size,seed=random.randint(0,9), coordenates=random.randint(0,9), direction=random.randint(0,1))
        barco.value = aux
        return place_boat(barco, mapa, 0)
    
    # horizontal placement
    if barco.direction == 0:
        i : int = 0
        aux : int = 0
        for i in range(barco.size):
            
            # try to place the boat in the right direction
            if aux == 0:
                if barco.coordenates + i < mapa.y and mapa.grid[barco.seed][barco.coordenates + i] == 0:
                    mapa.grid[barco.seed][barco.coordenates + i] = barco.value
           
                # if fails, erase the placed parts
                else:
                    j = i - 1
                    while(j >= 0):
                        if barco.coordenates + j < mapa.y and mapa.grid[barco.seed][barco.coordenates + j] == barco.value:
                            mapa.grid[barco.seed][barco.coordenates + j] = 0
                        j-=1
                    aux+=1

            # try to place the boat in left direction
            elif aux == 1:
                if barco.coordenates - i >= 0 and mapa.grid[barco.seed][barco.coordenates - i] == 0:
                    mapa.grid[barco.seed][barco.coordenates - i] = barco.value

                # if fails, erase the placed parts
                else:
                    j = i - 1
                    while(j >= 0):
                        if barco.coordenates - j >= 0 and mapa.grid[barco.seed][barco.coordenates - j] == barco.value:
                            mapa.grid[barco.seed][barco.coordenates - j] = 0
                        j -=1
                    
                    aux+=1
                    # and try to place in vertical direction
                    barco.direction = not barco.direction
                    return place_boat(barco, mapa, time + 1) 

    # vertical placement    
    if barco.direction == 1:
        i : int = 0
        aux : int = 0

        for i in range(barco.size):

            # try to place the boat in down direction
            if aux == 0:
                if barco.seed + i < mapa.x and mapa.grid[barco.seed + i][barco.coordenates] == 0:
                    mapa.grid[barco.seed + i][barco.coordenates] = barco.value

                # if fails, erase the placed parts
                else:
                    j = i - 1
                    while(j >= 0):
                        if barco.seed + j < mapa.x and mapa.grid[barco.seed + j][barco.coordenates] == barco.value:
                            mapa.grid[barco.seed + j][barco.coordenates] = 0
                        j-=1
                    aux+=1
            
            # try to place the boat in up direction
            elif aux == 1:
                if barco.seed - i >= 0 and mapa.grid[barco.seed - i][barco.coordenates] == 0:
                    mapa.grid[barco.seed - i][barco.coordenates] = barco.value

                # if fails, erase the placed parts
                else:
                    j = i - 1
                    while(j >= 0):
                        if barco.seed - j >= 0 and mapa.grid[barco.seed - j][barco.coordenates] == barco.value:
                            mapa.grid[barco.seed - j][barco.coordenates] = 0
                        j-=1
                    aux+=1
                    barco.direction = not barco.direction
                    return place_boat(barco, mapa, time + 1)


barco = Boats.boat(3,seed=random.randint(0,10),coordenates=random.randint(0,10), direction=random.randint(0,1))
mapa = Map.Map(10,10)
barco.value = 7
mapa.create_grid()

create_boats(2)
for i in range(len(boat_list)):
    print(boat_list[i].value, boat_list[i].seed, boat_list[i].coordenates, boat_list[i].direction)
    place_boat(boat_list[i],mapa,0)
    
print(mapa.grid)
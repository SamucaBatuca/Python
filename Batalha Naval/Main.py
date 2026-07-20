import numpy as np
import Boats
import Game_map as Map
import random

boat_list = []
tabletop : Map.Tabletop
map: Map.Map


def game(mode:int):
    bullets : int
    # settings for the game mode
    match mode:
        case 1:
            create_boats(4)
            map = Map.Map(5,5)
            tabletop = Map.Tabletop(5,5)
            tabletop.create_grid()
            map.create_grid()
            bullets = 18
        case 2:
            create_boats(5)
            create_boats(3)
            map = Map.Map(10,10)
            tabletop = Map.Tabletop(10,10)
            tabletop.create_grid()
            map.create_grid()
            bullets = 32
        case 3:
            for i in range(2):
                create_boats(5)
            create_boats(3)
            map = Map.Map(10,10)
            tabletop = Map.Tabletop(10,10)
            tabletop.create_grid()
            map.create_grid()
            bullets = 32
    
    # game starts
    while(bullets):
        aux : int = 0
        tabletop.display

        match aux:
            case 1:
                print("This is out of our range, Sir. Please, shoot again.")
            case 2:
                print("You already shoot this location, Sir. Please, shoot again.")


        cx,cy = int(input(f"You have {bullets} bullets remaining.\nInform the coordenate (X,Y) of the next shot, Sir:\nAnswer: ").split())

        if cx > tabletop.x or cy > tabletop.y:
            aux = 1
        elif map.grid[cy][cx] != 0 and tabletop.grid != '~':
            aux = 2
        elif map.grid[cy][cx] != 0:
            aux = map.grid[cy][cx]
            tabletop.grid[cy][cx] = aux
            aux = 0
            bullets-=1
        else:
            tabletop.grid[cy][cx] = '~'
        




            


def create_boats(quantity: int):
    for i in range(quantity):
        barco = Boats.boat(i+1,seed=random.randint(0,9),coordenates=random.randint(0,9), direction=random.randint(0,1))
        barco.value = i+1
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
        while (i < barco.size):
            
            # try to place the boat in the right direction
            if aux == 0:
                if barco.coordenates + i < mapa.x and mapa.grid[barco.seed][barco.coordenates + i] == 0 :
                    mapa.grid[barco.seed][barco.coordenates + i] = barco.value
                    i+=1
           
                # if fails, erase the placed parts
                else:
                    j = i
                    while(j >= 0):
                        if barco.coordenates + j < mapa.x and mapa.grid[barco.seed][barco.coordenates + j] == barco.value:
                            mapa.grid[barco.seed][barco.coordenates + j] = 0
                        j-=1
                    i = 0
                    aux+=1

            # try to place the boat in left direction
            elif aux == 1:
                if barco.coordenates - i >=0 and mapa.grid[barco.seed][barco.coordenates - i] == 0 :
                    mapa.grid[barco.seed][barco.coordenates - i] = barco.value
                    i+=1

                # if fails, erese the placed parts
                else:
                    j = i
                    while(j >= 0):
                        if barco.coordenates - j >= 0 and mapa.grid[barco.seed][barco.coordenates - j] == barco.value:
                            mapa.grid[barco.seed][barco.coordenates - j] = 0
                        j -=1
                    i = 0
                    aux+=1
                    # and try to place in vertical direction
                    barco.direction = not barco.direction
                    return place_boat(barco, mapa, time + 1) 

    # vertical placement    
    
    if barco.direction == 1:
        i : int = 0
        aux : int = 0

        while (i < barco.size):

            # try to place the boat in down direction
            if aux == 0:

                if barco.seed + i < mapa.y and mapa.grid[barco.seed + i][barco.coordenates] == 0 :
                    mapa.grid[barco.seed + i][barco.coordenates] = barco.value
                    i+=1

                # if fails, erase the placed parts
                else:
                    j = i
                    while(j >= 0):
                        if barco.seed + j < mapa.y and mapa.grid[barco.seed + j][barco.coordenates] == barco.value:
                            mapa.grid[barco.seed + j][barco.coordenates] = 0
                        j-=1
                    i = 0
                    aux+=1
            
            # try to place the boat in up direction
            elif aux == 1:
                if barco.seed - i >= 0 and mapa.grid[barco.seed -i][barco.coordenates] == 0 :
                    mapa.grid[barco.seed - i][barco.coordenates] = barco.value
                    i+=1

                # if fails, erase the placed parts
                else:
                    j = i
                    while(j >= 0):
                        if barco.seed - j >= 0 and mapa.grid[barco.seed - j][barco.coordenates] == barco.value:
                            mapa.grid[barco.seed - j][barco.coordenates] = 0
                        j-=1
                    i = 0
                    aux+=1
                    barco.direction = not barco.direction
                    return place_boat(barco, mapa, time + 1)


def menu(op:int):
    aux : int
    
    match op:
        case 0:
            print("~"*60)
            print("\t\tWelcome to the battleship!")
            print("\t\t   Select the game mode:")
            print("\t1) Easy \t2) Medium \t3) Hard\n\n")
            print("~"*60)
            print("\033[2A", end='')                    # move the cursor 2 lines up
            while True:
                

                try:
                    aux = int(input("\033[2KAnswer: "))
                    print("\033[2B",end='')             # move the cursor 2 lines down
                    break
                except ValueError:
                    print("\033[5A")
                    print("\033[K\t  Wrong choice. Please, choose again:")
                    print("\t1) Easy \t2) Medium \t3) Hard\n")
                    #print("\033[1B",end='')
                    

            if aux > 3 or aux < 0:
                while(aux > 3 or aux < 0):
                    print("\033[6A")
                    print("\033[K\t  Wrong choice. Please, choose again:")
                    print("\t1) Easy \t2) Medium \t3) Hard\n")
                    aux = int(input("\033[KAnswer: "))
                    print("\033[2B",end='')
            game(aux)
        case 1:
            create_boats()  


menu(0)


""""
create_boats(5)
for i in range(len(boat_list)):
    print(boat_list[i].value, boat_list[i].seed, boat_list[i].coordenates, boat_list[i].direction)
    place_boat(boat_list[i],mapa,0)
    
"""

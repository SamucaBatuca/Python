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
            map = Map.Map(5,5)
            tabletop = Map.Tabletop(5,5)
            tabletop.create_grid()
            map.create_grid()
            create_boats(3, map.x-1, 0)
            create_boats(2, map.x-1, 0)
            bullets = 18
        case 2:
            map = Map.Map(10,10)
            tabletop = Map.Tabletop(10,10)
            tabletop.create_grid()
            map.create_grid()
            create_boats(5, map.x-1, 0)
            create_boats(3, map-1, 0)
            bullets = 32
        case 3:
            map = Map.Map(10,10)
            tabletop = Map.Tabletop(10,10)
            tabletop.create_grid()
            map.create_grid()
            for i in range(2):
                create_boats(5, map.x-1, 0)
            create_boats(3, map.x-1, 0)
            bullets = 32
    
    goal : int = 0
    for i in range(len(boat_list)):
        print(boat_list[i].value, boat_list[i].seed, boat_list[i].coordenates, boat_list[i].direction)
        goal += boat_list[i].value
        place_boat(boat_list[i],map,0)

    aux : int = 0
    # game starts
    while(bullets):
        
        print(map.grid)
        tabletop.display()

        match aux:
            case 1:
                print("This is out of our range, Sir. Please, shoot again.")
            case 2:
                print("You already shoot this location, Sir. Please, shoot again.")


        cx,cy = input(f"You have {bullets} bullets remaining.\nInform the coordenate (X,Y) of the next shot, Sir:\nAnswer: ").split()
        cx = int(cx)
        cy = int(cy)

        if (cx < 0) or (cy < 0) or (cx >= map.x) or (cy >= map.x):
            aux = 1
        elif map.grid[cy][cx] != 0 and tabletop.grid[cy+1][cx+1] == '~':
            aux = map.grid[cy][cx]
            print(aux)
            tabletop.grid[cy+1][cx+1] = aux
            aux = 0
            bullets-=1
        elif tabletop.grid[cy+1][cx+1] != '~':
            aux = 2
        else:
            tabletop.grid[cy+1][cx+1] = 'X'
            bullets -= 1
        




            


def create_boats(quantity: int, len:int, unit: int):

    print("OLHA O LEN: ", len)
    
    if unit == 0:
        for i in range(quantity-1):
            barco = Boats.boat(i+1,seed=random.randint(0,len),coordenates=random.randint(0,len), direction=random.randint(0,1))
            barco.value = i+1
            boat_list.append(barco)
        else:
            barco = Boats.boat(quantity,seed=random.randint(0,len),coordenates=random.randint(0,len), direction=random.randint(0,1))
            barco.value = quantity
            boat_list.append(barco) 

def place_boat(barco: Boats.boat, mapa: Map.Map, time: int):

    if time >= 2:
        aux = barco.value
        barco = Boats.boat(size=barco.size,seed=random.randint(0,mapa.x-1), coordenates=random.randint(0,mapa.x-1), direction=random.randint(0,1))
        barco.value = aux
        return place_boat(barco, mapa, 0)
    
    # horizontal placement
    if barco.direction == 0:
        i : int = 0
        aux : int = 0
        while (i < barco.size):
            print("horizontal: ",barco.value, i)
            
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
                if barco.coordenates - i >= 0 and mapa.grid[barco.seed][barco.coordenates - i] == 0 :
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
            print("vertical: ",barco.value, i)
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
                if barco.seed - i >= 0 and mapa.grid[barco.seed - i][barco.coordenates] == 0 :
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

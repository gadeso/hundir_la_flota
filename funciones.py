import numpy as np
import random

def generar_tablero(tablero, lista_barcos):
    
    for eslora in lista_barcos:
        
        while True:
            
            # 'N' - 'S' - 'E' - 'O'
            orient = random.choice(['N', 'S', 'E', 'O'])

            # Posicion inicial del barco
            current_pos = np.random.randint(10, size = 2)
            
            fila = current_pos[0]
            col = current_pos[1]
            
            # Recogemos las 4 posiciones colindantes a current_pos
            coors_posiN = tablero[fila:fila - eslora:-1, col]
            coors_posiE = tablero[fila, col: col + eslora]
            coors_posiS = tablero[fila:fila + eslora, col]
            coors_posiO = tablero[fila, col: col - eslora:-1]
            
            
            # Comprobamos si esas posiciones son validas
            # Orientacion Norte
            if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                tablero[fila:fila - eslora:-1, col] = 'O'
                break

            # Orientacion Este
            elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                tablero[fila, col: col + eslora] = 'O'
                break

            # Orientacion Sur
            elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                tablero[fila:fila + eslora, col] = 'O'
                break

            # Orientacion Oeste
            elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                tablero[fila, col: col - eslora:-1] = 'O'
                break

            # No cumple con las dimensiones del tablero, o hay un barco ahi
            # Probamos con otra coordenada
            else:
                continue
    return tablero

#Función que muestre adónde van los disparos del jugador
def disparo_jugador(tablero,a,b):
    
    posicion = tablero[a,b]
    
    if posicion == "O":
        vidas = vidas - 1
        posicion = "X"
    
    else:
        posicion = "-"
    
    return tablero, vidas

#Función que muestre adónde van los disparos del PC
def disparo_enemigo(tablero):
    
    a = random.choice([0,1,2,3,4,5,6,7,8,9])
    b = random.choice([0,1,2,3,4,5,6,7,8,9])
    print(a,b)
    
    posicion = tablero[a,b]
    
    if posicion == "O":
        print(1)
        vidas = vidas - 1
        posicion = "X"
    
    else:
        print(2)
        posicion = "-"
   
    return tablero, vidas
import numpy as np
import random
from variables import BARCOS, tablero_disparos, tablero_jugador, tablero_pc, MENU

def generar_tablero(tablero, lista_barcos):
    for eslora in lista_barcos:
        while True:
            orient = random.choice(['N', 'S', 'E', 'O'])
            current_pos = np.random.randint(10, size=2)
            fila, col = current_pos
            
            if orient == 'N' and fila - eslora >= 0 and 'O' not in tablero[fila-eslora+1:fila+1, col]:
                tablero[fila-eslora+1:fila+1, col] = 'O'
                break
            elif orient == 'E' and col + eslora <= 10 and 'O' not in tablero[fila, col:col+eslora]:
                tablero[fila, col:col+eslora] = 'O'
                break
            elif orient == 'S' and fila + eslora <= 10 and 'O' not in tablero[fila:fila+eslora, col]:
                tablero[fila:fila+eslora, col] = 'O'
                break
            elif orient == 'O' and col - eslora >= 0 and 'O' not in tablero[fila, col-eslora+1:col+1]:
                tablero[fila, col-eslora+1:col+1] = 'O'
                break
    return tablero

def disparo_jugador(tablero_enemigo, x, y):
    if tablero_enemigo[x, y] == 'O':
        tablero_enemigo[x, y] = 'X'
        return tablero_enemigo, True
    elif tablero_enemigo[x, y] == ' ':
        tablero_enemigo[x, y] = '-'
        return tablero_enemigo, False
    else:
        print(MENU["repetido"])
        return tablero_enemigo, False

def disparo_enemigo(tablero_jugador):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if tablero_jugador[x, y] == 'O':
            tablero_jugador[x, y] = 'X'
            return tablero_jugador, True
        elif tablero_jugador[x, y] == ' ':
            tablero_jugador[x, y] = '-'
            return tablero_jugador, False
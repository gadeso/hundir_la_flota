"""Variables para el battleship"""

import numpy as np

BARCOS = [1,1,1,1,2,2,2,3,3,4]

DIMENSION_TABLERO = (10,10)

ORIENTACION = ('N', 'S', 'E', 'O')

RELLENO_TABLERO = {
    "agua" : " ",
    "hit" : "X",
    "miss" : "-",
    "barco" : "O"
}

MENU = {
    "intro": "\nBATTLESHIP UNDER THE BRIDGE®\n\t !Bienvenido!\n \
    \n El primero en hundir los barcos enemigos ganará. Los barcos son posicionados de manera aleatoria.\n\
    4 barcos de 1 posición\n\
    3 barcos de 2 posiciones\n\
    2 barcos de 3 posiciones\n\
    1 barco de 4 posiciones\n"+
    "!Prepárate para jugar¡\n",

    "boom": "\n¡BOOM! \n¡Repite turno!",
    "fallo": "\n¡FALLO! \n Cambio de turno",
    "repetido": "\nYa has usado esta coordenada, prueba con otra",
    
    "ganar": "\nWinner winner, chicken dinner. ¡Felicitaciones!",
    "perder": "\n¡Has perdido!"
}

tablero_jugador = np.full(fill_value = ' ', shape = (10, 10))

tablero_pc = np.full(fill_value = ' ', shape = (10, 10))

tablero_disparos = np.full(fill_value = ' ', shape = (10, 10))
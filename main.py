import numpy as np
from funciones import generar_tablero, disparo_enemigo, disparo_jugador
from variables import BARCOS, tablero_disparos, tablero_jugador, tablero_pc, MENU

#Generar tableros
tablero_enemigo = generar_tablero(tablero_pc,BARCOS)
tablero_j1 = generar_tablero(tablero_jugador,BARCOS)

#Instrucciones del juego
print(MENU["intro"])

#Juego funcionando
vidas = 20

while vidas > 0:
    print(f"Tu tablero se ve así: \n{tablero_j1}\n")
    print(f"Tablero enemigo: \n{tablero_disparos}\n")
    introducir_disparo = input("Escribe una coordenada del 0 al 9 sin decimales (x,x):\n")
    
    if introducir_disparo == "O":
        print(MENU["boom"])
        
    elif introducir_disparo == " ":
        print(MENU["fallo"])
        
    else:
        print(MENU["repetido"])
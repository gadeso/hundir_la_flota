import numpy as np
from funciones import generar_tablero, disparo_enemigo, disparo_jugador
from variables import BARCOS, tablero_disparos, tablero_jugador, tablero_pc, MENU

# Generar tableros
tablero_enemigo = generar_tablero(tablero_pc, BARCOS)
tablero_j1 = generar_tablero(tablero_jugador, BARCOS)

# Instrucciones del juego
print(MENU["intro"])

# Juego funcionando
vidas_j1 = sum(BARCOS)
vidas_pc = sum(BARCOS)

while vidas_j1 > 0 and vidas_pc > 0:
    print(f"Tu tablero se ve así: \n{tablero_j1}\n")
    print(f"Tablero enemigo: \n{tablero_disparos}\n")
    
    # Solicitar disparo del jugador
    x, y = map(int, input("Escribe una coordenada del 0 al 9 en el formato x,y:\n").split(','))
    
    tablero_enemigo, hit_j1 = disparo_jugador(tablero_enemigo, x, y)
    if hit_j1:
        vidas_pc -= 1
        print(MENU["boom"])
    else:
        print(MENU["fallo"])
    
    # Disparo del enemigo
    tablero_j1, hit_pc = disparo_enemigo(tablero_j1)
    if hit_pc:
        vidas_j1 -= 1

# Determinar el ganador
if vidas_j1 > 0:
    print(MENU["ganar"])
else:
    print(MENU["perder"])
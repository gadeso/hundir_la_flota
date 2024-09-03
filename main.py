import numpy as np
import time
from funciones import generar_tablero, disparo_enemigo, disparo_jugador, verificar_barco_destruido
from variables import BARCOS, tablero_disparos, tablero_jugador, tablero_pc, MENU

# Generar tableros
tablero_enemigo = generar_tablero(tablero_pc, BARCOS)
tablero_j1 = generar_tablero(tablero_jugador, BARCOS)

# Instrucciones del juego
print(MENU["intro"])

# Juego funcionando
vidas_j1 = sum(BARCOS)
vidas_pc = sum(BARCOS)

turno_jugador = True  # El jugador comienza

while vidas_j1 > 0 and vidas_pc > 0:
    print(f"Tu tablero se ve así: \n{tablero_j1}\n")
    print(f"Tablero de tus disparos: \n{tablero_disparos}\n")
    
    if turno_jugador:
        # Solicitar disparo del jugador
        x, y = map(int, input("Escribe una coordenada del 0 al 9 en el formato x,y:\n").split(','))
        
        tablero_enemigo, hit_j1, barco_destruido = disparo_jugador(tablero_enemigo, x, y)
        if hit_j1:
            vidas_pc -= 1
            tablero_disparos[x, y] = 'X'
            print(MENU["boom"])
            if barco_destruido:
                print("¡Has derribado un barco enemigo por completo!")
            if vidas_pc == 0:  # Si las vidas del enemigo llegan a 0, el jugador gana
                break
            continue  # Permitir que el jugador dispare nuevamente
        else:
            tablero_disparos[x, y] = '-'
            print(MENU["fallo"])
            turno_jugador = False  # Cambia el turno al enemigo
    
    else:
        # Disparo del enemigo
        tablero_j1, hit_pc = disparo_enemigo(tablero_j1)
        if hit_pc:
            vidas_j1 -= 1
            print("\nEl enemigo ha acertado en uno de tus barcos!\n")
            if vidas_j1 == 0:  # Si las vidas del jugador llegan a 0, el enemigo gana
                break
            continue  # Permitir que el enemigo dispare nuevamente
        else:
            print("\nEl enemigo ha fallado su disparo.\n")
            turno_jugador = True  # Cambia el turno al jugador

    time.sleep(1.5)  # Pausa de 1.5 segundos antes del siguiente turno

# Determinar el ganador
if vidas_j1 > 0:
    print(MENU["ganar"])
else:
    print(MENU["perder"])

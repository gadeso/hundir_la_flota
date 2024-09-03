# Battleship Under the Bridge®
¡Bienvenido! Este es un emocionante juego de batalla naval en el que el primero en hundir todos los barcos enemigos gana. La versión que estás por descargar es una simulación del clásico juego de "Hundir la Flota" hecha en Python.

## Cómo Iniciar el Juego
Para comenzar a jugar, asegúrate de tener Python instalado en tu sistema. Luego, simplemente abre tu terminal o línea de comandos, navega hasta el directorio donde se encuentran los archivos del juego y ejecuta:
#### python main.py
Esto hará que el juego se inicie. Serás recibido con una pantalla de bienvenida e instrucciones.

## Cómo Jugar
Tu objetivo es hundir todos los barcos del enemigo antes de que él hunda los tuyos. El tablero del enemigo se genera aleatoriamente, y tu tarea es adivinar la ubicación de sus barcos disparando coordenadas en el tablero.

## Instrucciones
Se te mostrarán dos tableros:
Tu propio tablero, donde se encuentran tus barcos.
Un tablero de disparos, donde podrás ver tus intentos de ataque al enemigo.

Introducción de Coordenadas:
Para disparar a un barco enemigo, debes ingresar coordenadas en el formato x,y (por ejemplo, 3,4).
Las coordenadas deben estar entre 0 y 9, siendo 0 la esquina superior izquierda del tablero.

Turnos:
El juego se desarrolla por turnos. Si aciertas en un disparo y golpeas un barco enemigo, puedes volver a disparar.
Si fallas, el turno pasa al enemigo.

Resultado del Disparo:
Si aciertas en un barco, se marcará una "X" en el tablero de disparos.
Si fallas, se marcará un "-".
El enemigo seguirá las mismas reglas contra ti.

Fin del Juego:
El juego termina cuando uno de los dos jugadores hunde todos los barcos de su oponente.


#### Nota Importante: Aunque puedes ver el tablero enemigo, esto solo es para que entiendas cómo funciona la lógica del código. En un juego real, el tablero enemigo debería estar oculto.


## Lógica del Juego
Este juego utiliza varias técnicas y métodos para simular el comportamiento de una batalla naval. A continuación se describen algunas de las principales características.

1. Generación del Tablero
Los barcos se colocan en el tablero de manera aleatoria. La lógica garantiza que los barcos no se superpongan ni se salgan de los límites del tablero.
Se utilizan orientaciones al azar (N, S, E, O) para decidir cómo se colocarán los barcos en el tablero.
2. Manejo de Turnos y Disparos
El jugador y el enemigo alternan turnos para disparar.
Si un jugador acierta en un disparo, puede continuar disparando. Si falla, el turno pasa al otro jugador.
Se utiliza una pausa entre los turnos para mejorar la experiencia del usuario, haciendo que el juego se sienta más dinámico y realista.
3. Validación de Coordenadas
El juego verifica que las coordenadas introducidas estén dentro del rango permitido (0 a 9). Si las coordenadas no son válidas, se muestra un mensaje de error, y se le pide al jugador que intente nuevamente.
4. Detección de Barcos Destruidos
Después de cada acierto, el juego verifica si se ha hundido un barco completo. Si es así, se notifica al jugador con un mensaje.

## Métodos y Herramientas Utilizadas
- Numpy: Se utilizó para crear y manejar los tableros de juego, ya que permite manipular matrices de manera eficiente.
- Random: Se utilizó para la colocación aleatoria de barcos y para los disparos aleatorios del enemigo.
- Time: Se utilizó para añadir pausas entre las acciones del juego, mejorando así la experiencia del usuario.


Si tienes alguna consulta o sugerencia, puedes contactarme a través de mi correo personal: desousaga@gmail.com

¡Disfruta del juego y que tengas mucha suerte hundiendo la flota enemiga!

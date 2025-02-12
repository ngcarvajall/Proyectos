import random

def inicializar_juego():
    juego_proceso = True
    jugador1 = [input('Jugador 1: Dame tu nombre'), 'X']
    jugador2 = [input('Jugador 2: Dame tu nombre'), 'O']
    jugador_actual = random.randint(0, 1)
    tablero = [["-" for _ in range(3)] for _ in range(3)]

    return juego_proceso, jugador1, jugador2, jugador_actual, tablero

def conversion(tablero_input):
    diccionario = {'X': 1, 'O': 0}
    tablero = []
    for fila in tablero_input:
        nueva_fila = [diccionario.get(celda, celda) for celda in fila]
        tablero.append(nueva_fila)
    return tablero

def revisar_tablero(board):
    for i in range(3):
        row = [board[i][j] for j in range(3)]

        if ('-' not in row):
            cross_wins = sum(row) == 3
            zero_wins = sum(row) == 0
        
            if cross_wins:
                return 1  # Ganador Jugador 1
            if zero_wins:
                return 0  # Ganador Jugador 2

    # Revisar columnas
    for j in range(3):
        column = [board[i][j] for i in range(3)]
        
        if ('-' not in column):
            cross_wins = sum(column) == 3
            zero_wins = sum(column) == 0
            if cross_wins:
                return 1  # Ganador Jugador 1
            if zero_wins:
                return 0  # Ganador Jugador 2

    # Revisar diagonal principal
    principal_diag = [board[i][i] for i in range(3)]
    if ('-' not in principal_diag):
        cross_wins = sum(principal_diag) == 3
        zero_wins = sum(principal_diag) == 0
        if cross_wins:
            return 1  # Ganador Jugador 1
        if zero_wins:
            return 0  # Ganador Jugador 2
        
    # Revisar diagonal secundaria
    inverse_diag = [board[i][-1 - i] for i in range(3)]
    if ('-' not in inverse_diag):
        cross_wins = sum(inverse_diag) == 3
        zero_wins = sum(inverse_diag) == 0
        if cross_wins:
            return 1  # Ganador Jugador 1
        if zero_wins:
            return 0  # Ganador Jugador 2

    # Revisar si el tablero está lleno
    tablero_lleno = esta_lleno(board)

    if tablero_lleno:
        return 2  # Empate
    else:
        return -1  # El juego sigue

def esta_lleno(board):
    for fila in board:
        if '-' in fila:  # Si hay alguna celda vacía, el tablero no está lleno
            return False
    return True  # Si no se encontró ninguna celda vacía, el tablero está lleno

def mov_player1(tablero):
    while True:
        fila = int(input('Jugador 1 (X): elige la fila (0-2): '))
        columna = int(input('Jugador 1 (X): elige la columna (0-2): '))
        if fila in range(3) and columna in range(3) and tablero[fila][columna] == '-':
            tablero[fila][columna] = 'X'
            break
        else:
            print('Esta posición no es válida. Intenta de nuevo.')
    return tablero

def mov_player2(tablero):
    while True:
        fila = int(input('Jugador 2 (O): elige la fila (0-2): '))
        columna = int(input('Jugador 2 (O): elige la columna (0-2): '))
        if fila in range(3) and columna in range(3) and tablero[fila][columna] == '-':
            tablero[fila][columna] = 'O'
            break
        else:
            print('Esta posición no es válida. Intenta de nuevo.')
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()  

def iniciar_juego():
    juego_proceso, jugador1, jugador2, jugador_actual, tablero = inicializar_juego()
    estado = -1

    while estado == -1:
        mostrar_tablero(tablero)
        
        if jugador_actual == 0:  # Jugador 1 es el jugador actual
            tablero = mov_player1(tablero)
        else:  # Jugador 2 es el jugador actual
            tablero = mov_player2(tablero)

        # Revisar si el juego termina después del movimiento
        tablero_numeros = conversion(tablero)  # Aquí conviertes el tablero
        estado = revisar_tablero(tablero_numeros)  # Revisamos el estado del tablero
        
        if estado == 0:
            mostrar_tablero(tablero)  # Mostrar el tablero final antes de anunciar el ganador
            print(f'Ganador: {jugador2[0]} (Jugador 2)')
            break
        elif estado == 1:
            mostrar_tablero(tablero)  # Mostrar el tablero final antes de anunciar el ganador
            print(f'Ganador: {jugador1[0]} (Jugador 1)')
            break
        elif estado == 2:
            mostrar_tablero(tablero)  # Mostrar el tablero final antes de anunciar el empate
            print('Empate')
            break

        jugador_actual = 1 - jugador_actual  # Cambiar entre 0 y 1
import random
LISTADO = ['python', 'desarrollador', 'programacion'] ### constante
def jugar():

    dibujo_ahorcado = [
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
        /|   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
        /|\  |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
        /|\  |
        /    |
            |
        =========
        ''',
    ]

    palabra_elegida = list(random.choice(LISTADO))
    palabra_oculta =['_']*len(palabra_elegida)
    num_intentos = 6
    lista_abecedario = list('abcdefghijklmnñopqrstuvwxyz')
    letras_descartadas = []


    print('BIENVENIDO AL JUEGO DEL AHORCADO, Hackio Edition 😎 \n')
    print('Reglas del juego: Introduce letras para adivinar la palabra oculta .')
    print(f'Tienes {num_intentos} intentos. ¡Buena suerte!')

    while num_intentos > 0 and '_' in palabra_oculta:
        mostrar_estado(num_intentos,letras_descartadas,palabra_oculta,dibujo_ahorcado)
        print('-----')
        letra_elegida = input('Introduce una letra:').lower()

        while not opcion_letra(letra_elegida, lista_abecedario, palabra_oculta,letras_descartadas):
            letra_elegida = input('Introduce otra letra').lower()

        if letra_elegida in palabra_elegida:
            gestion(letra_elegida,palabra_elegida,palabra_oculta)
            print('Has acertado la letra')
        else: 
            print('Te has equivocado chaval')
            letras_descartadas.append(letra_elegida)
            num_intentos -= 1
            ### debo de agregar la visual del ahorcado (hago un contador de la lista de dibujos que vaya aumentando )
            ### me falta imprimir la palabra completa
    if '_' not in palabra_oculta: ### agregar que cuando los intentos y el contador sean iguales, se pierde
        print('\n🏆¡ENHORABUENA!🏆\n🏆¡HAS GANADO EL JUEGO!🏆')
        mostrar_estado(num_intentos,letras_descartadas,palabra_oculta,dibujo_ahorcado)
    else:
        mostrar_estado(num_intentos,letras_descartadas,palabra_oculta,dibujo_ahorcado)
        print(f'\n ¡Mejor suerte la próxima!'
            '''\n
        +---+
        |   |
        💀   |
        /|\  |
        / \  |
            |
        =========
        ''')

def mostrar_estado(intentos, descartes,ocultas,dibujo):

    print(f'Intentos restantes: {intentos}')
    print(f'Letras descartadas: {", ".join(descartes)}\n')
    print(f'Palabra: {" ".join(ocultas)}\n')
    print(dibujo[6 - intentos])


def opcion_letra(letra, abecedario,pal_oculta,let_descartadas):
    if len(letra) != 1:
        print('Has seleccionado más de una letra')
        return False
    elif letra not in abecedario:
        print('Has seleccionado una letra fuera del abecedario')
        return False
    elif letra in pal_oculta:
        print('Esta letra ya la has acertado')
        return True
    elif letra in let_descartadas:
        print('Esta letra ya la habías dicho')
        return False
    else:
        return True

def gestion(letra,p_e,p_o):
        for i in range(len(p_e)):
            if p_e[i] == letra:
                p_o[i] = letra
                p_e[i] = '_'


import random
PREGUNTAS_NELSON = {
    "preguntas_geografia": [
        {"Pregunta": "¿Cuál es la capital de República Dominicana?", "Respuestas": {"La Romana": False, "Santo Domingo": True, "Samaná": False, "Punta Cana": False}},
        {"Pregunta": "¿Cuál es la capital de España?", "Respuestas": {"Barcelona": False, "Valencia": False, "Madrid": True, "Zaragoza": False}},
        {"Pregunta": "¿Qué océano baña las costas de África occidental?", "Respuestas": {"Océano Atlántico": True, "Océano Índico": False, "Océano Pacífico": False, "Mar Mediterráneo": False}},
        {"Pregunta": "¿Cuál es el río más largo del mundo?", "Respuestas": {"Nilo": True, "Amazonas": False, "Yangtsé": False, "Misisipi": False}},
        {"Pregunta": "¿Qué país tiene más islas en el mundo?", "Respuestas": {"Suecia": True, "Canadá": False, "Indonesia": False, "Noruega": False}}
    ],
    "preguntas_historia": [
        {"Pregunta": "¿En qué año se descubrió América?", "Respuestas": {"1493": False, "1492": True, "1776": False, "1505": False}},
        {"Pregunta": "¿En qué año se independizó la República Dominicana?", "Respuestas": {"1822": False, "1821": False, "1844": True, "1865": False}},
        {"Pregunta": "¿Quién fue el primer presidente de Estados Unidos?", "Respuestas": {"George Washington": True, "Thomas Jefferson": False, "Abraham Lincoln": False, "John Adams": False}},
        {"Pregunta": "¿Qué civilización construyó las pirámides de Egipto?", "Respuestas": {"Egipcios": True, "Mayas": False, "Aztecas": False, "Griegos": False}},
        {"Pregunta": "¿Qué evento marcó el inicio de la Segunda Guerra Mundial?", "Respuestas": {"La invasión de Polonia": True, "La firma del Tratado de Versalles": False, "La caída de Berlín": False, "El ataque a Pearl Harbor": False}}
    ],
    "preguntas_entretenimiento": [
        {"Pregunta": '¿Cuál es el nombre del actor que protagonizó la película "Joker"?', "Respuestas": {"Ryan Gosling": False, "Heath Ledger": False, "Joaquin Phoenix": True, "Hugh Jackman": False}},
        {"Pregunta": "¿Quién canta la canción 'Thriller'?", "Respuestas": {"Michael Jackson": True, "Prince": False, "Madonna": False, "Elton John": False}},
        {"Pregunta": "¿En qué año se estrenó la película 'Titanic'?", "Respuestas": {"1997": True, "1998": False, "1995": False, "2000": False}},
        {"Pregunta": "¿Qué película ganó el Oscar a Mejor Película en 2020?", "Respuestas": {"Parasite": True, "1917": False, "Joker": False, "Once Upon a Time in Hollywood": False}},
        {"Pregunta": "¿Quién es el creador de la serie 'Game of Thrones'?", "Respuestas": {"George R.R. Martin": True, "J.K. Rowling": False, "Joss Whedon": False, "Stephen King": False}}
    ],
    "preguntas_futbol": [
        {"Pregunta": "¿En qué país se celebró el Mundial de fútbol de 2014?", "Respuestas": {"Alemania": False, "Brasil": True, "Sudáfrica": False, "España": False}},
        {"Pregunta": "¿Qué equipo ha ganado el mayor número de UEFA Champions League?", "Respuestas": {"Real Madrid": True, "FC Barcelona": False, "AC Milan": False, "Juventus": False}},
        {"Pregunta": "¿Quién es el máximo goleador de la historia de los Mundiales?", "Respuestas": {"Pele": False, "Miroslav Klose": True, "Ronaldo": False, "Diego Maradona": False}},
        {"Pregunta": "¿Qué país ganó la Eurocopa 2016?", "Respuestas": {"Portugal": True, "Francia": False, "Alemania": False, "España": False}},
        {"Pregunta": "¿En qué año se fundó la FIFA?", "Respuestas": {"1904": True, "1920": False, "1930": False, "1950": False}}
    ]
}

def preguntados_function(preguntas = PREGUNTAS_NELSON):
    contador = 0

    while contador < 10:
        eleccion = int(input(f"Elige una categoría para probar tus conocimientos: 1. Geografía 2. Historia 3. Entretenimiento 4. Deporte\n"))

        if eleccion == 1:
            pregunta_aleatoria = random.choice(preguntas["preguntas_geografia"])
        elif eleccion == 2:
            pregunta_aleatoria = random.choice(preguntas["preguntas_historia"])
        elif eleccion == 3:
            pregunta_aleatoria = random.choice(preguntas["preguntas_entretenimiento"])
        elif eleccion == 4:
            pregunta_aleatoria = random.choice(preguntas['preguntas_futbol'])
        else:
            print("Categoría no disponible aún.")
            continue

        print(pregunta_aleatoria["Pregunta"])
        for k in pregunta_aleatoria["Respuestas"]:
            print(k)

        respuesta = input('Elige una respuesta:')

        if pregunta_aleatoria["Respuestas"].get(respuesta) == True:
            print('¡Ganaste un punto!')
            contador += 1
            print(f'Llevas {contador} respuestas correctas')
        else:
            print('Te has equivocado, has respondido', respuesta)
            print('Hasta aquí todo por hoy') ### añadir algo más
            break

    if contador == 10:
        print('¡Eres el puto amo!')
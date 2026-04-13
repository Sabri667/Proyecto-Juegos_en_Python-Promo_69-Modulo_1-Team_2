
preguntas_y_respuestas_trivial = {'¿Quién es el mejor amigo de Harry Potter?': 'Ron Weasley', '¿Qué animal es la mascota de Harry?' : 'Una lechuza', '¿Cuántas casas hay en Hogwarts?' : '4', '¿A qué casa pertenece Luna Lovegood?' : 'Ravenclaw', '¿Cuál es el hechizo que sirve para hacer levitar objetos?' : 'Wingardium Leviosa', '¿Quién es el descubridor de la Piedra Filosofal?' : 'Nicolas Flamel', '¿En qué andén debes coger el Hogwarts Express?': 'Andén 9 3/4', '¿Qué clase de criaturas son los trabajadores de Gringotts?' : 'Duendes', '¿En qué lugar se celebra la segunda prueba del Torneo de los Tres Magos?' : 'Lago Negro', '¿Cuántos libros tiene la saga de Harry Potter?' : '7' }
#Diccionario final con número de letra asignada.
preguntas_y_respuestas_trivial = {'¿Quién es el mejor amigo de Harry Potter?': 'A: Ron Weasley', '¿Qué animal es la mascota de Harry?' : 'C: Una lechuza', '¿Cuántas casas hay en Hogwarts?' : 'A: 4', '¿A qué casa pertenece Luna Lovegood?' : 'B: Ravenclaw', '¿Cuál es el hechizo que sirve para hacer levitar objetos?' : 'B: Wingardium Leviosa', '¿Quién es el descubridor de la Piedra Filosofal?' : 'B: Nicolas Flamel', '¿En qué andén debes coger el Hogwarts Express?': 'A: Andén 9 3/4', '¿Qué clase de criaturas son los trabajadores de Gringotts?' : 'D: Duendes', '¿En qué lugar se celebra la segunda prueba del Torneo de los Tres Magos?' : 'A: Lago Negro', '¿Cuántos libros tiene la saga de Harry Potter?' : 'C:7' }
respuestas_correctas = list(preguntas_y_respuestas_trivial.values()) #Hacemos una lista con las respuestas correctas (valores del diccionario).
#Ponemos en un diccionario nuevo la pregunta como key y todas las respuestas como values.
preguntas_y_respuestas_ABCD = {'¿Quién es el mejor amigo de Harry Potter?': ['A: Ron Weasley','B: Neville Longbottom', 'C: Hermione Granger', 'D: Draco Malfoy'], '¿Qué animal es la mascota de Harry?' : ['A: Un gato', 'B: Una rata', 'C: Una lechuza', 'D: Un sapo'], '¿Cuántas casas hay en Hogwarts?' : ['A: 4', 'B: 3', 'C: 5', 'D: 1'], '¿A qué casa pertenece Luna Lovegood?' : ['A: Gryffindor', 'B: Ravenclaw', 'C: Hufflepuff', 'D: Slytherin'], '¿Cuál es el hechizo que sirve para hacer levitar objetos?' : ['A: Incendio','B: Wingardium Leviosa','C: Protego', 'D: Flotatum'], '¿Quién es el descubridor de la Piedra Filosofal?' : ['A: James Filosofal','B: Nicolas Flamel', 'C: Albus Dumbledore', 'D: Harry Potter'], '¿En qué andén debes coger el Hogwarts Express?': ['A: Andén 9 3/4', 'B: Andén 3 9/4', 'C: Andén 11', 'D: Andén 4 3/9'], '¿Qué clase de criaturas son los trabajadores de Gringotts?' : ['A: Elfos', 'B: Gnomos', 'C: Enanos', 'D: Duendes'], '¿En qué lugar se celebra la segunda prueba del Torneo de los Tres Magos?' : ['A: Lago Negro', 'B: Lavabo de prefectos', 'C: Laberinto', 'D: Se suspende la prueba'], '¿Cuántos libros tiene la saga de Harry Potter?' : ['A: 6', 'B: 8', 'C: 7','D: Aún no se han publicado todos.'] }
respuestas_totales = list(preguntas_y_respuestas_ABCD.values()) #Convertimos todas las respuestas en una lista.
import random #importamos la librería random para poder escoger una pregunta aleatoria.

preguntas=list(preguntas_y_respuestas_ABCD.keys()) #Creamos la lista 'preguntas' con las keys del diccionario.
opciones = ['A', 'B', 'C', 'D'] #Acotamos los valores que aceptaremos como válidos.
#Hacemos una pequeña introducción al juego, para hacerlo más divertido y personalizado:
nombre_usuario = input('Introduce tu nombre para empezar a jugar.')
print (f'¡Hola, {nombre_usuario}! Empecemos el juego.')
print ('Para ganar el juego deberás acertar 5 preguntas. Si fallas 3 habrás perdido.')
print ('Empecemos...')

import time
time.sleep(3)
aciertos = 0 #|--> definimos variables que representan las reglas del juego.
errores = 0  #|

while True: #---> Empieza el juego: un bucle en el que te hará preguntas y solo se romperá al acertar 5 o fallar 3.
    a=random.choice(preguntas)#Escoge una pregunta aleatoria de la lista
    print(a) #Nos la imprime para que la podamos ver
    for i in preguntas_y_respuestas_ABCD[a]: #Buscará dentro del diccionario la pregunta que ha escogido
            print(f"{i}") #y nos imprime i, es decir, las values (respuestas)
    
    print ('----------------------') #unas rayas para separar y que quede más visual
    respuesta_usuario= input('Responde A, B, C o D:') #Aquí el usuario da su respuesta
    respuesta_usuario = respuesta_usuario.upper()#por si la diera en minúscula...
    while respuesta_usuario not in opciones: # y esto por si pone algo que no es ABCD
        print ('Respuesta no válida. Responda de nuevo.')#pero sin cambiar la pregunta
        respuesta_usuario = (input('Responde A, B, C o D:'))
        respuesta_usuario = respuesta_usuario.upper()
    print (f'Tu respuesta es la {respuesta_usuario}. Vamos a comprobar si es correcta...')
    time.sleep(3)
    preguntas.remove(a) #Eliminamos la pregunta de la lista para evitar que se repita.

   
    if respuesta_usuario in preguntas_y_respuestas_trivial[a]: #Buscará si la opción introducida (ABCD) coincide con la asignada al value (A. Ron Weasley)
        print ('¡Has acertado!')
        aciertos += 1 #suma 1 a los aciertos y visualiza numero de aciertos y errores.
        print('')
        print(f'Total de aciertos = {aciertos}. Total de errores = {errores}.')
        print ('----------------------') 
        time.sleep(2)
        print('Siguiente pregunta:')
        time.sleep(2)
        if aciertos == 5: #le damos un comando para que rompa el bucle cuando llegue al numero de aciertos
            print('*********************************')
            print ('¡Has ganado!:)')

            break
        
    elif respuesta_usuario not in preguntas_y_respuestas_trivial[a]: #lo mismo para cuando falle
        print ('Vaya... Has fallado.')
        errores += 1
        print (f'Total de aciertos = {aciertos}. Total de errores = {errores}.')
        print ('----------------------')
        if errores == 3:
            print('*********************************')
            print ('Has perdido... :(')
            break
            

print ('Fin del juego.')

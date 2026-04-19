import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# --- 1. PREPARACIÓN DE DATOS ---

preguntas_dict = {
    '¿Quién es el mejor amigo de Harry Potter?': ['A: Ron Weasley','B: Neville Longbottom', 'C: Hermione Granger', 'D: Draco Malfoy'],
    '¿Qué animal es la mascota de Harry?' : ['A: Un gato', 'B: Una rata', 'C: Una lechuza', 'D: Un sapo'],
    '¿Cuántas casas hay en Hogwarts?' : ['A: 4', 'B: 3', 'C: 5', 'D: 1'],
    '¿A qué casa pertenece Luna Lovegood?' : ['A: Ravenclaw', 'B: Gryffindor', 'C: Hufflepuff', 'D: Slytherin'],
    '¿Cuál es el hechizo que sirve para hacer levitar objetos?' : ['A: Incendio','B: Wingardium Leviosa','C: Protego', 'D: Flotatum'],
    '¿Quién es el descubridor de la Piedra Filosofal?' : ['A: Nicolas Flamel','B: James Filosofal', 'C: Albus Dumbledore', 'D: Harry Potter'],
    '¿En qué andén debes coger el Hogwarts Express?': ['A: Andén 9 3/4', 'B: Andén 3 9/4', 'C: Andén 11', 'D: Andén 4 3/9'],
    '¿Qué clase de criaturas son los trabajadores de Gringotts?' : ['A: Duendes', 'B: Elfos', 'C: Gnomos', 'D: Enanos'],
    '¿En qué lugar se celebra la segunda prueba del Torneo de los Tres Magos?' : ['A: Lago Negro', 'B: Lavabo de prefectos', 'C: Laberinto', 'D: Se suspende la prueba'],
    '¿Cuántos libros tiene la saga de Harry Potter?' : ['A: 7', 'B: 6', 'C: 8','D: Aún no se han publicado todos.']
}

soluciones = {
    '¿Quién es el mejor amigo de Harry Potter?': 'A',
    '¿Qué animal es la mascota de Harry?': 'C',
    '¿Cuántas casas hay en Hogwarts?': 'A',
    '¿A qué casa pertenece Luna Lovegood?': 'A',
    '¿Cuál es el hechizo que sirve para hacer levitar objetos?': 'B',
    '¿Quién es el descubridor de la Piedra Filosofal?': 'A',
    '¿En qué andén debes coger el Hogwarts Express?': 'A',
    '¿Qué clase de criaturas son los trabajadores de Gringotts?': 'A',
    '¿En qué lugar se celebra la segunda prueba del Torneo de los Tres Magos?': 'A',
    '¿Cuántos libros tiene la saga de Harry Potter?': 'A'
}

# --- 2. VARIABLES DE ESTADO ---
preguntas_lista = list(preguntas_dict.keys())
aciertos = 0
errores = 0
pregunta_actual = ""
nombre_jugador = ""

# --- 3. FUNCIONES DE CONTROL ---

def iniciar():
    global nombre_jugador
    nombre_jugador = simpledialog.askstring("Harry Potter QUIZ", "Estimadx mago o bruja, \n¿Cuál es tu nombre?")

    if not nombre_jugador: nombre_jugador = "Jugador 1"
    ventana.title(f"Trivial de Harry Potter - Jugador: {nombre_jugador}")
    messagebox.showinfo('','NORMAS DEL JUEGO:\n Debes acertar 5 preguntas para ganar.\nSi por el contrario fallas 3 veces, perdiste.') 
    siguiente_pregunta()


def siguiente_pregunta():
    global pregunta_actual
    #restaurar_colores()
    
    # Comprobar condiciones de fin de juego
    if aciertos == 5:
        messagebox.showinfo("¡VICTORIA!", f"¡Increíble {nombre_jugador}!. ¡Listo/a para los TIMOs!")
        ventana.destroy()
        return
    if errores == 3:
        messagebox.showerror("DERROTA", f"Lo siento {nombre_jugador}, 3 fallos... ¡A Azkaban!")
        ventana.destroy()
        return

    if preguntas_lista:
        pregunta_actual = random.choice(preguntas_lista)
        preguntas_lista.remove(pregunta_actual)
        
        lbl_pregunta.config(text=pregunta_actual)
        opciones = preguntas_dict[pregunta_actual]
        
        btn_a.config(text=opciones[0])
        btn_b.config(text=opciones[1])
        btn_c.config(text=opciones[2])
        btn_d.config(text=opciones[3])
        
        lbl_status.config(text=f"Aciertos: {aciertos} | Errores: {errores}")
    else:
        messagebox.showinfo("Fin", "Se acabaron las preguntas.")
        ventana.destroy()

def comprobar(letra, boton_pulsado):
    global aciertos, errores
    
    if letra == soluciones[pregunta_actual]:
        aciertos += 1
        messagebox.showwarning("Acierto","¡Cooorrecto!\n¡Sigue así!")
        ventana.after(500, siguiente_pregunta) # Espera medio segundo y pasa a la siguiente
    else:
        errores += 1
        messagebox.showwarning("Fallo", f"¡Casiii...!\n La respuesta correcta era la {soluciones[pregunta_actual]}")
        siguiente_pregunta()

# --- 4. DISEÑO DE LA INTERFAZ ---
ventana = tk.Tk()
ventana.geometry("550x600")
ventana.configure(bg="#7F0909")

# Estilo de la pregunta
lbl_pregunta = tk.Label(ventana, text="Cargando...", font=("Verdana", 25, "bold"), 
                        wraplength=400, justify="center", height=4,bg="#D4AF37", fg="#7F0909")
lbl_pregunta.pack(pady=30)

# Contenedor para los botones (así quedan ordenaditos)
frame_respuestas = tk.Frame(ventana, bg="#7F0909")
frame_respuestas.pack(pady=10)

# Botones con Lambda. Fíjate que ahora pasamos la letra Y el propio objeto botón
btn_a = tk.Button(frame_respuestas, text="", width=50, height=2, font=("Arial", 25), bg="#D4AF37", fg="#7F0909", activebackground="#EFBC2F", activeforeground="#7F0909", command=lambda: comprobar("A", btn_a))
btn_a.pack(pady=5)

btn_b = tk.Button(frame_respuestas, text="", width=50, height=2, font=("Arial", 25),bg="#D4AF37", fg="#7F0909", activebackground="#EFBC2F", activeforeground="#7F0909", command=lambda: comprobar("B", btn_b))
btn_b.pack(pady=5)

btn_c = tk.Button(frame_respuestas, text="", width=50, height=2, font=("Arial", 25),bg="#D4AF37", fg="#7F0909", activebackground="#EFBC2F", activeforeground="#7F0909", command=lambda: comprobar("C", btn_c))
btn_c.pack(pady=5)

btn_d = tk.Button(frame_respuestas, text="", width=50, height=2, font=("Arial", 25), bg="#D4AF37", fg="#7F0909", activebackground="#EFBC2F", activeforeground="#7F0909", command=lambda: comprobar("D", btn_d))
btn_d.pack(pady=5)

# Barra de estado inferior
lbl_status = tk.Label(ventana, text="", font=("Arial", 20, "italic"), bg="#7F0909", fg="#EFBC2F")
lbl_status.pack(side="bottom", pady=20)

# Lanzar el inicio
ventana.after(100, iniciar)
ventana.mainloop()

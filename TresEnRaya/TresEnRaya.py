import tkinter as tk
from tkinter import messagebox, simpledialog

def imprimir_tablero(tablero):
    for i in range(3):
        fila = tablero[i]
        print(" | ".join(fila))
        if i < 2:
            print("---------------")

def mover_en_L1(movimiento, posicion, indice, ficha):
    if movimiento == posicion:
        L1[indice] = ficha
        L1_juego[indice] = ' · '
        posiciones_tablero.remove(posicion)

def mover_en_L2(movimiento, posicion, indice, ficha):
    if movimiento == posicion:
        L2[indice] = ficha
        L2_juego[indice] = ' · '
        posiciones_tablero.remove(posicion)

def mover_en_L3(movimiento, posicion, indice, ficha):
    if movimiento == posicion:
        L3[indice] = ficha
        L3_juego[indice] = ' · '
        posiciones_tablero.remove(posicion)

def ganar2(ficha, jugador):
    if (L1.count(ficha) == 3 or L2.count(ficha) == 3 or L3.count(ficha) == 3 or
        L1[0]==ficha and L2[0]==ficha and L3[0]==ficha or
        L1[1]==ficha and L2[1]==ficha and L3[1]==ficha or
        L1[2]==ficha and L2[2]==ficha and L3[2]==ficha or
        L1[0]==ficha and L2[1]==ficha and L3[2]==ficha or
        L1[2]==ficha and L2[1]==ficha and L3[0]==ficha):
        messagebox.showinfo("Fin del juego", f"¡Enhorabuena {jugador}, HAS GANADO! :)")
        return True
    return False

def empatar():
    if len(posiciones_tablero) == 0:
        messagebox.showinfo("Fin del juego", f"{jugador1} y {jugador2}... ¡Habéis empatado!")
        return True
    return False

# ========== INICIALIZACIÓN DE LAS ESTRUCTURAS ==========

# Tablero de juego (lista de listas con espacios)
L1 = ['   ', '   ', '   ']
L2 = ['   ', '   ', '   ']
L3 = ['   ', '   ', '   ']
tablero_partida = [L1, L2, L3]

# Tablero de referencia (con números)
L1_juego = [' 1 ', ' 2 ', ' 3 ']
L2_juego = [' 4 ', ' 5 ', ' 6 ']
L3_juego = [' 7 ', ' 8 ', ' 9 ']
tablero_movimientos = [L1_juego, L2_juego, L3_juego]

# Posiciones disponibles (se van eliminando)
posiciones_tablero = ["1","2","3","4","5","6","7","8","9"]

# Nombres de jugadores 

ventana_temp = tk.Tk()
ventana_temp.withdraw()  

jugador1 = simpledialog.askstring("Jugadores", "Nombre del Jugador 1:") or "Jugador 1"
jugador2 = simpledialog.askstring("Jugadores", "Nombre del Jugador 2:") or "Jugador 2"

ventana_temp.destroy()# ========== INTERFAZ TKINTER ==========

class TatetiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya - Tu Tateti")
        self.root.geometry("350x450")
        
        # Variables de estado
        self.turno = ' X '   # ficha con espacios como en tu código
        self.jugador_actual = jugador1
        
        # Etiqueta de turno
        self.label_turno = tk.Label(root, text=f"Turno: {self.jugador_actual} {self.turno}", font=("Arial", 14))
        self.label_turno.pack(pady=10) #.pack() posiciona el elemento.pady=10 añade espacio vertical.  

        # Marco para los botones del tablero
        frame = tk.Frame(root) #los agrupa
        frame.pack() #aca los contiene
        
        # Crear 3x3 botones, cada uno asociado a una posición
        self.botones = []
        for i in range(3):
            fila_botones = []
            for j in range(3):
                # Número de casilla (1..9)
                num = i * 3 + j + 1
                btn = tk.Button(frame, text="   ", font=("Arial", 20), width=4, height=2,
                                command=lambda n=num: self.hacer_movimiento(n))
                btn.grid(row=i, column=j, padx=2, pady=2)
                fila_botones.append(btn)
            self.botones.append(fila_botones)
        
        # Mostrar tablero de referencia (opcional)
        self.mostrar_referencia()
    
    def mostrar_referencia(self):
        """Muestra en consola las posiciones (como hacías antes)"""
        print("Posiciones de las casillas:\n")
        imprimir_tablero(tablero_movimientos)
    
    def hacer_movimiento(self, num):
        """Se ejecuta cuando un jugador clickea un botón"""
        pos = str(num)
        
        # Validar que la casilla esté disponible
        if pos not in posiciones_tablero:
            messagebox.showwarning("\nMovimiento inválido", "Casilla no disponible o ya ocupada.")
            return
        
        # Colocar la ficha usando las funciones mover_en_Lx
        # Llamamos a las tres de cada fila (solo una hará efecto)
        mover_en_L1(pos, '1', 0, self.turno)
        mover_en_L1(pos, '2', 1, self.turno)
        mover_en_L1(pos, '3', 2, self.turno)
        mover_en_L2(pos, '4', 0, self.turno)
        mover_en_L2(pos, '5', 1, self.turno)
        mover_en_L2(pos, '6', 2, self.turno)
        mover_en_L3(pos, '7', 0, self.turno)
        mover_en_L3(pos, '8', 1, self.turno)
        mover_en_L3(pos, '9', 2, self.turno)
        
        # Actualizar el texto del botón (mostrar la ficha sin espacios extra)
        fila = (num-1) // 3
        col = (num-1) % 3
        self.botones[fila][col].config(text=self.turno.strip(), state="disabled")
        
        # Verificar si hay ganador (usando tu función ganar2)
        if ganar2(self.turno, self.jugador_actual):
            self.root.quit()  # Cierra la ventana después de mostrar el mensaje
            return
        
        # Verificar empate
        if empatar():
            self.root.quit()
            return
        
        # Cambiar turno
        self.turno = ' O ' if self.turno == ' X ' else ' X '
        self.jugador_actual = jugador2 if self.jugador_actual == jugador1 else jugador1
        self.label_turno.config(text=f"Turno: {self.jugador_actual} {self.turno}")
    
# ========== EJECUCIÓN ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = TatetiGUI(root)
    root.mainloop()
    print("\nFin del juego. Gracias por participar.")

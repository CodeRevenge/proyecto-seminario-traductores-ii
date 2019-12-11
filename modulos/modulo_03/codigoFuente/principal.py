# -*- coding: utf-8 -*-
import sys
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from src.analizadorSintactico import AnalizadorSintactico
from src.analizadorSemantico import AnalizadorSemantico

def abrir_archivo():
    root = Tk()
    root.withdraw()
    direccion = ""
    instrucciones = ''
    while not direccion:
        direccion = askopenfilename(initialdir="./tests/", filetypes=[("C", "*.c")])
        if not direccion:
            if not messagebox.askretrycancel(message="No se selecciono ningun archivo, ¿Desea reintentarlo?", title="No se selecciono archivo"):
                return False
    archivo = open(direccion, "r")
    instrucciones = archivo.readlines()
    instrucciones = ' '.join(map(str.strip,instrucciones))
    archivo.close()
    return instrucciones

def main():
    cadena = abrir_archivo()
    if not cadena:
        print("El código compilo correctamente")
        return
    else:
        analizador = AnalizadorSintactico()
        # resultado = analizador.analizadorSintactico(cadena)
        resultado = analizador.analizadorSintacticoEnteros(cadena)
        if resultado:
            analizador.arbol.arbol.muestra()
            analizadorSem = AnalizadorSemantico(analizador.arbol.arbol)
            print("El código compilo correctamente")
    # Fin del if-else

if __name__ == '__main__':
    main()
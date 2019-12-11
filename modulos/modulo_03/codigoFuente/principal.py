# -*- coding: utf-8 -*-
import sys
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from src.analizadorSintactico import AnalizadorSintactico

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
        return

    # cadena = input('Escribe la cadena a analizar: ')
    # Verificamos que la cadena no este vacia
    if len(cadena) <= 0:
        print(cadena + " No es una cadena valida")
    else:
        analizador = AnalizadorSintactico()
        # resultado = analizador.analizadorSintactico(cadena)
        resultado = analizador.analizadorSintacticoEnteros(cadena)
        if resultado:
            analizador.arbol.arbol.muestra()
            print("El código compilo correctamente")
    # Fin del if-else

if __name__ == '__main__':
    main()
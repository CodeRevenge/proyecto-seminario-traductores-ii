# -*- coding: utf-8 -*-
import sys
from analizadorSintactico import AnalizadorSintactico

def main():

    # Para evitar errores de compativilidad verificamos la version de python
    # Valido para python 3.x o superiores
    if sys.version_info >= (3,0):
        # Recibimos cadena y la convertimos a un string
        cadena = str(input("Escribe una cadena: "))
    else:
        # Valido para python 2.x
        # cadena = str(raw_input("Escribe una cadena: "))
        pass

    
    # Imprimimos unos titulos para mejor entendimiento
    print("\n\nResultado del analisis sintáctico:")

    # Verificamos que la cadena no este vacia
    if len(cadena) <= 0:
        print(cadena + " No es una cadena valida")
    else:
        analizador = AnalizadorSintactico()
        resultado = analizador.analizadorSintactico(cadena)
        analizador.analizadorSintacticoEnteros(cadena)
        if resultado:
            print("\n\nLa cadena es valida\n\n")
        else:
            print("\n\nLa cadena es invalida\n\n")
    # Fin del if-else

if __name__ == '__main__':
    main()
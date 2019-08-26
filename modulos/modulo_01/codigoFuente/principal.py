import sys
from analizadorLexico import AnalizadorLexico

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
    # Verificamos que la cadena no este vacia
    if len(cadena) <= 0:
        print(cadena + " No es una cadena valida")
    else:
        # Creamos un objeto de tipo AnalizadorLexico y lo inicializamos con el valor de la cande
        analizador = AnalizadorLexico(cadena)

        # Imprimimos unos titulos para mejor entendimiento
        print("\n\n")
        print("Resultado del analisis lexico:")
        print('{:*<75}'.format(""))
        print('{:<30}'.format("Simbolo") + '{:<30}'.format("Tipo") + '{:<5}'.format("Codigo de Tipo"))

        # Realizamos un ciclo que continue hasta que el simobolo sea un $
        while analizador.caracter != "$":
            # Analizamos el primer simbolo de la cadena
            analizador.siguienteSimbolo()
            # Imprimimos el simbolo junto al tipo de cadena
            print('{:<30}'.format(analizador.simbolo) + '{:<30}'.format(analizador.tipoCadena(analizador.tipo)) + '{:<5}'.format(str(analizador.tipo)))
    # Fin del if-else

if __name__ == '__main__':
    main()
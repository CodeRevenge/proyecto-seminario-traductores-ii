from src.analizadorLexico import AnalizadorLexico
from src.arbol import Arbol

class ReglasSintacticas:
    def __init__(self):
        self.tabla_lr = []
        self.extra = []
        self.id_reglas = []
        self.long_reglas = []
        self.id_regla_int = []
        self.leer_reglas()

    def leer_reglas(self):
        file = open('data/compilador.lr','r')
        for linea in file.readlines():
            linea = linea.split('\t')
            if len(linea) > 3:
                for index, item in enumerate(linea):
                    try:
                        linea[index] = int(item)
                    except ValueError:
                        raise Exception('La tabla lr contiene valores invalidos. {}'.format(item))
                self.tabla_lr.append(linea)
            else:
                for index, item in enumerate(linea):
                    try:
                        linea[index] = int(item.strip())
                    except ValueError:
                        linea[index] = item.strip()
                if len(linea) == 1:
                    self.id_regla_int.append(linea[0])
                    self.long_reglas.append(0)
                    self.id_reglas.append(0)
                elif len(linea) == 2:
                    self.id_regla_int.append(linea[1])
                    self.long_reglas.append(0)
                    self.id_reglas.append(linea[0])
                elif len(linea) == 3:
                    self.id_regla_int.append(linea[0])
                    self.long_reglas.append(linea[1])
                    self.id_reglas.append(linea[2])
                self.extra.append(linea)
        file.close()

class AnalizadorSintactico(ReglasSintacticas):
    def __init__(self):
        ReglasSintacticas.__init__(self)
        self.entradas = []
        self.arbol = Arbol()

    def analizadorSintacticoEnteros(self, cadena):
        self.cadena = cadena
        self.tuplas = []
        self.pilaEnteros = [23,0]
        self.pilaCadenas = [23,0]
        self.entradasEnteros = []
        self.tipos = []
        self.entradasSimbolos = []
        self.item_selected = None
        self.salidaEntero = 0

        self.analizarSimbolos()

        self.temp_tuplas = self.tuplas.copy()

        while self.salidaEntero != -1:
            
            if self.temp_tuplas:
                self.item_selected = self.temp_tuplas[0]
            # print(self.item_selected)
            self.salidaEntero = self.tabla_lr[self.pilaEnteros[-1]][self.entradasEnteros[0]]

            if self.salidaEntero < -1:
                temp = []
                for i in range(self.long_reglas[-1*(self.salidaEntero+2)]*2):
                    self.pilaEnteros.pop()
                    a = self.pilaCadenas.pop()
                    if i % 2 == 1:
                        temp.append(a)
                self.entradasEnteros.insert(0,self.id_regla_int[-1*(self.salidaEntero+2)])
                self.entradasSimbolos.insert(0,self.id_reglas[-1*(self.salidaEntero+2)])
                self.tipos.insert(0,self.id_reglas[-1*(self.salidaEntero+2)])
                self.arbol.insertarNodo(self.tipos[0], self.entradasEnteros[0], temp)
            elif self.salidaEntero == -1:
                return True
            elif self.salidaEntero == 0:
                print('Error: La sintaxis no es correcta en el/la {} "{}"'.format(self.item_selected[2],self.item_selected[0]))
                return False
            else:
                self.pilaEnteros.append(self.entradasEnteros[0])
                self.pilaEnteros.append(self.salidaEntero)
                self.pilaCadenas.append(self.entradasSimbolos[0])
                self.pilaCadenas.append(self.salidaEntero)
                self.entradasEnteros.pop(0)
                self.entradasSimbolos.pop(0)
                self.tipos.pop(0)
            if self.temp_tuplas:
                self.temp_tuplas.pop(0)

        return True

    def analizarSimbolos(self):
        # Creamos un objeto de tipo AnalizadorLexico y lo inicializamos con el valor de la cande
        analizador = AnalizadorLexico(self.cadena)

        # Realizamos un ciclo que continue hasta que el simobolo sea un $
        while analizador.caracter != "$":
            self.tuplas.append(analizador.siguienteSimbolo())
            # Agrega tuplas del estilo (Simbolo:str, #Tipo:int, NombreTipo:str)
        self.tuplas.append(("$",23,"PESO"))

        for x in range(len(self.tuplas)):
            self.entradas.append(self.tuplas[x])
            self.entradasSimbolos.append(self.tuplas[x][0])
            self.entradasEnteros.append(self.tuplas[x][1])
            self.tipos.append(self.tuplas[x][2])

    
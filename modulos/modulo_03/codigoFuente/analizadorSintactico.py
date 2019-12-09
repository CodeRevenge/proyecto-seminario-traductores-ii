from analizadorLexico import AnalizadorLexico

class ElementoPila:
    def __init__(self):
        pass

class ReglaSumaRecursiva:
    def __init__(self):
        self.ID_REGLAS = ["E","E"]
        self.ID_REGLAS_ENTEROS = [-2,-2]
        self.LONG_REGLAS = [3,1]
        self.TABLA_LR_UNO = [["d2",0,0,1],[0,0,"r0",0],[0,"d3","r2",0],["d2",0,0,4],[0,0,"r1",0]]
        self.TABLA_LR_UNO_ENTEROS = [[2,0,0,1],[0,0,-1,0],[0,3,-3,0],[2,0,0,4],[0,0,-2,0]]
        self.TIPOS = {
            "Identificador":0,
            "Mas":1,
            "PESO":2,
            "E":3
        }

class ReglasSintacticas:
    def __init__(self):
        self.tabla_lr = []
        self.extra = []
        self.id_reglas = []
        self.long_reglas = []
        self.id_regla_int = []
        self.leer_reglas()

    def leer_reglas(self):
        file = open('compilador.lr','r')
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

    def analizadorSintacticoEnteros(self, cadena):
        self.cadena = cadena
        self.tuplas = []
        self.pilaEnteros = [23,0]
        self.entradasEnteros = []
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
                for _ in range(self.long_reglas[-1*(self.salidaEntero+2)]*2):
                    self.pilaEnteros.pop(-1)
                self.entradasEnteros.insert(0,self.id_regla_int[-1*(self.salidaEntero+2)])
            elif self.salidaEntero == -1:
                return True
            elif self.salidaEntero == 0:
                print('Error: La sintaxis no es correcta en el/la {} "{}"'.format(self.item_selected[2],self.item_selected[0]))
                return False
            else:
                self.pilaEnteros.append(self.entradasEnteros[0])
                self.pilaEnteros.append(self.salidaEntero)

                self.entradasEnteros.pop(0)
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
            self.entradasEnteros.append(self.tuplas[x][1])

    # def imprimirPaso(self, paso):
    #     print('{:<8}'.format(str(paso)) + '{:<30}'.format(self.joinList2Str(self.pila)) + '{:<30}'.format(self.joinEntradas(self.entradas)) + '{:<8}'.format(str(self.salida)))

    # def imprimirPasoEntero(self, paso):
    #     print('{:<8}'.format(str(paso)) + '{:<30}'.format(self.joinList2StrEnteros(self.pilaEnteros)) + '{:<30}'.format(self.joinEntradasEnteros(self.entradasEnteros)) + '{:<8}'.format(str(self.salidaEntero)))

    # def joinList2Str(self, lista):
    #     s = []
    #     for i in range(len(lista)):
    #         if type(lista[i]) is int:
    #             s.append(str(lista[i]))
    #         else:
    #             s.append(lista[i])
    #     res = "".join(s)
    #     return(res)

    # def joinEntradas(self, entradas):
    #     s = []
    #     for i in range(len(entradas)):
    #         s.append(entradas[i][0])
    #     res = "".join(s)
    #     return(res)

    # def joinList2StrEnteros(self, lista):
    #     s = []
    #     for i in range(len(lista)):
    #         if type(lista[i]) is int:
    #             s.append(str(self.TIPOS_ENTEROS.get(lista[i])))
    #         else:
    #             s.append(lista[i])
    #     res = "".join(s)
    #     return(res)
    
    # def joinEntradasEnteros(self, entradas):
    #     s = []
    #     for i in range(len(entradas)):
    #         s.append(str(self.TIPOS_ENTEROS.get(entradas[i],'Unknow')))
    #     res = "".join(s)
    #     return(res)
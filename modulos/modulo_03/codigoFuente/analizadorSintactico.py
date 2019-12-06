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

class AnalizadorSintactico(ReglaSumaRecursiva):
    def __init__(self):
        ReglaSumaRecursiva.__init__(self)
        self.SALIDAS_STR = {
            "d2":2,
            "d3":3,
            "r0":-1,
            "r1":-2,
            "r2":-3
        }

        self.TIPOS_ENTEROS = {
            0:0,
            1:1,
            2:2,
            3:3,
            4:4,
            5:1,
            "E":3
        }

        self.cadena = ""
        self.tuplas = []
        self.pila = ["$",0]
        self.pilaEnteros = [2,0]
        self.entradas = []
        self.entradasEnteros = []
        self.salida = ""
        self.salidaEntero = 0

        

    def analizadorSintactico(self, cadena):
        self.cadena = cadena

        self.tuplas = []
        self.pila = ["$",0]
        self.entradas = []
        self.salida = ""

        self.analizarSimbolos()

        print('{:^76}'.format("Desplazamientos y reducciones"))
        print('{:<8}'.format("Paso") + '{:<30}'.format("Pila") + '{:<30}'.format("Entradas") + '{:<8}'.format("Salida"))
        print('{:*^76}'.format(""))
        pasos = 1
        while self.salida != self.TABLA_LR_UNO[1][2]:
            if self.entradas[0] == "E":
                self.salida = self.TABLA_LR_UNO[self.pila[-1]][self.TIPOS.get(self.entradas[0])]
                self.salidaEntero = self.salida
                self.imprimirPaso(pasos)
            else:
                self.salida = self.TABLA_LR_UNO[self.pila[-1]][self.TIPOS.get(self.entradas[0][2])]
                self.salidaEntero = self.SALIDAS_STR.get(self.salida, 0)
                self.imprimirPaso(pasos)

            if self.salidaEntero < -1:
                for _ in range(2*self.LONG_REGLAS[-1*(self.salidaEntero+2)]):
                    self.pila.pop(-1)
                self.entradas.insert(0,self.ID_REGLAS[-1*(self.salidaEntero+2)])
            elif self.salidaEntero == -1:
                return True
            elif self.salidaEntero == 0:
                return False
            else:
                self.pila.append(self.entradas[0][0])
                self.pila.append(self.salidaEntero)

                self.entradas.pop(0)
            pasos += 1

        return True

    def analizadorSintacticoEnteros(self, cadena):
        self.cadena = cadena
        self.tuplas = []
        self.pilaEnteros = [2,0]
        self.entradasEnteros = []
        self.salidaEntero = 0

        self.analizarSimbolos()

        # print("\n\n")
        # print('{:^76}'.format("Enteros"))
        # print('{:<8}'.format("Paso") + '{:<30}'.format("Pila") + '{:<30}'.format("Entradas") + '{:<8}'.format("Salida"))
        # print('{:*^76}'.format(""))
        pasos = 1
        while self.salidaEntero != self.TABLA_LR_UNO_ENTEROS[1][2]:

            self.salidaEntero = self.TABLA_LR_UNO_ENTEROS[self.pilaEnteros[-1]][self.TIPOS_ENTEROS.get(self.entradasEnteros[0])]
            self.imprimirPasoEntero(pasos)

            if self.salidaEntero < -1:
                for _ in range(2*self.LONG_REGLAS[-1*(self.salidaEntero+2)]):
                    self.pilaEnteros.pop(-1)
                self.entradasEnteros.insert(0,self.TIPOS_ENTEROS.get(self.ID_REGLAS[-1*(self.salidaEntero+2)]))
            elif self.salidaEntero == -1:
                return True
            elif self.salidaEntero == 0:
                return False
            else:
                self.pilaEnteros.append(self.entradasEnteros[0])
                self.pilaEnteros.append(self.salidaEntero)

                self.entradasEnteros.pop(0)
            pasos += 1

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

    def imprimirPaso(self, paso):
        print('{:<8}'.format(str(paso)) + '{:<30}'.format(self.joinList2Str(self.pila)) + '{:<30}'.format(self.joinEntradas(self.entradas)) + '{:<8}'.format(str(self.salida)))

    def imprimirPasoEntero(self, paso):
        print('{:<8}'.format(str(paso)) + '{:<30}'.format(self.joinList2StrEnteros(self.pilaEnteros)) + '{:<30}'.format(self.joinEntradasEnteros(self.entradasEnteros)) + '{:<8}'.format(str(self.salidaEntero)))

    def joinList2Str(self, lista):
        s = []
        for i in range(len(lista)):
            if type(lista[i]) is int:
                s.append(str(lista[i]))
            else:
                s.append(lista[i])
        res = "".join(s)
        return(res)

    def joinEntradas(self, entradas):
        s = []
        for i in range(len(entradas)):
            s.append(entradas[i][0])
        res = "".join(s)
        return(res)

    def joinList2StrEnteros(self, lista):
        s = []
        for i in range(len(lista)):
            if type(lista[i]) is int:
                s.append(str(self.TIPOS_ENTEROS.get(lista[i])))
            else:
                s.append(lista[i])
        res = "".join(s)
        return(res)
    
    def joinEntradasEnteros(self, entradas):
        s = []
        for i in range(len(entradas)):
            s.append(str(self.TIPOS_ENTEROS.get(entradas[i],'Unknow')))
        res = "".join(s)
        return(res)
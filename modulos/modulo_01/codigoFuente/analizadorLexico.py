class TipoCadena:
    "Clase que define los tipos de simbolos"
    def __init__(self):
        self.ERROR = -1
        self.IDENTIFICADOR = 0
        self.ENTERO = 1
        self.REAL = 2
        self.CADENA = 3
        self.TIPO = 4
        self.opSUMA = 5
        self.opRESTA = 6
        self.opMULTIPLICACION = 7
        self.opDIVISION = 8
        self.opOR = 9
        self.opAND = 10
        self.opNOT = 11
        self.opMAYORQ = 12
        self.opMENORQ = 13
        self.opMAYOROIGUAL = 14
        self.opMENOROIGUAL = 15
        self.opIGUAL = 16
        self.opESIGUAL = 17
        self.opESDIFERENTE = 18
        self.PUNTOYCOMA = 19
        self.COMA = 20
        self.PARENTESIOSABIERTO = 21
        self.PARENTESISCERRADO = 22
        self.LLAVAABIERTA = 23
        self.LLAVECERRADA = 24
        self.BRACKETABIERTO = 25
        self.BRACKETCERRADO = 26
        self.IF = 27
        self.WHILE = 28
        self.RETURN = 29
        self.ELSE = 30
        self.INT = 31
        self.FLOAT = 32
        self.PESO = 33

# class Estados:
#     "Clase que define los metodos de cada estado"
#     def __init__(self, caracter):
#         self.caracter = caracter

    

class AnalizadorLexico(TipoCadena):
    "Metodos para el analisis de cadenas"
    def __init__(self, cadena, indice = 0, continua = True, caracter = "", estado = 1, simbolo = "", tipo = -1, tipoCadenaMensaje = ""): 
        self.cadena = cadena

        self.indice = indice
        self.continua = continua
        self.caracter = caracter
        self.estado = estado

        self.simbolo = simbolo
        self.tipo = tipo

        self.tipoCadenaMensaje = tipoCadenaMensaje

        TipoCadena.__init__(self)

    def tipoCadena(self, tipo):
        self.tipoCadenaMensaje = ""

        switch = {
            self.ERROR: self.m_ERROR,
            self.IDENTIFICADOR: self.m_IDENTIFICADOR,
            self.ENTERO: self.m_ENTERO,
            self.REAL: self.m_REAL,
            self.CADENA: self.m_CADENA,

            self.PESO: self.m_PESO
        }

        switch[tipo]()

        return self.tipoCadenaMensaje

        

    def siguienteSimbolo(self):
        self.estado = 1
        self.continua = True
        self.simbolo = ""
        self.tipo = -1

        # Damos inicio al automata
        
        
        while self.continua:
            # Seleccionamos el siguiente caracter de la cadena
            self.caracter = self.siguienteCaracter()

            switch = {
                0: self.estado00,
                1: self.estado01,
                2: self.estado02,
                3: self.estado03,
                4: self.estado04,
                5: self.estado05,
                6: self.estado06,
                7: self.estado07,
                # 8: self.estado08,
                # 9: self.estado09,
                # 10: self.estado10,
                # 11: self.estado11,
                # 12: self.estado12,
                # 13: self.estado13,
                # 14: self.estado14,
                # 15: self.estado15,
                # 16: self.estado16,
                # 17: self.estado17,
                # 18: self.estado18,
                # 19: self.estado19,
                # 20: self.estado20
            }

            switch.get(self.estado, self.error)()

        # Terminamos el automata

        switch = {
            -1: self.error, # ERROR
            2: self.tipo00, # Identificador
            3: self.tipo01, # Entero
            5: self.tipo02, # Real
            7: self.tipo03, # Cadena

            33: self.tipo33 # Peso
        }

        switch.get(self.estado, self.error)()



    def siguienteCaracter(self):
        """Determina el siguiente caracter

        Si la cadena esta en el final regresa un simbolo $
        Si no, se incrementa el indice en uno y se regresa el caracter que tiene ese indice
        """
        if self.terminado():
            return "$"
        caracter = self.cadena[self.indice]
        self.indice += 1
        return caracter

    def siguienteEstado(self, estado):      
        self.estado = estado
        self.simbolo += self.caracter

        
    def retroceso(self):
        if not self.esPeso(self.caracter):
            self.indice -= 1
        self.continua = False
    
    # def encontrarEspacio(self):
    #     self.continua = False
    #     self.estado = -1
    #     if self.terminado():
    #         self.caracter = "$"
    #         return

    #     for x in range(self.indice, len(self.cadena)):
    #         self.simbolo += self.caracter + self.cadena[x]
    #         self.caracter = ""
    #         if self.esEspacio(self.cadena[x]):
    #             self.indice = x+1
    #             break

    def terminado(self):
        return self.indice >= len(self.cadena)

    # Definimos funciones que evaluan el tipo de caracter

    def esPeso(self, caracter):
        return caracter == "$"

    def esEspacio(self, caracter):
        return caracter == " "

    def esCaracter(self, caracter):
        return ord(caracter) == 32 or ord(caracter) == 33 or ord(caracter) >= 35 and ord(caracter) <= 126

    def esLetra(self, caracter):
        return caracter.isalpha() or caracter == "_"

    def esNumero(self, caracter):
        return caracter.isdigit()

    def esPunto(self, caracter):
        return caracter == "."
    
    def esComilla(self, caracter):
        return caracter == "\""
        
    def esSuma(self, caracter):
        return caracter == "+"

    def esResta(self, caracter):
        return caracter == "-"

    def esMultiplicacion(self, caracter):
        return caracter == "*"

    def esDivision(self, caracter):
        return caracter == "/"
    
    # Definimos todos los estados

    def estado00(self):
        self.continua = False

    def estado01(self):
        if self.esPeso(self.caracter):
            self.siguienteEstado(0)
        elif self.esLetra(self.caracter):
            self.siguienteEstado(2)
        elif self.esNumero(self.caracter):
            self.siguienteEstado(3)
        elif self.esComilla(self.caracter):
            self.siguienteEstado(6)
        elif self.esEspacio(self.caracter):
            self.estado = 1
        else:
            self.simbolo += self.caracter
            self.continua = False

    def estado02(self):
        if self.esLetra(self.caracter):
            self.siguienteEstado(2)
        elif self.esNumero(self.caracter):
            self.siguienteEstado(2)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado03(self):
        if self.esNumero(self.caracter):
            self.siguienteEstado(3)
        elif self.esPunto(self.caracter):
            self.tipo = -1
            self.siguienteEstado(4)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado04(self):
        if self.esNumero(self.caracter):
            self.siguienteEstado(5)
        else:
            self.retroceso()

    def estado05(self):
        if self.esNumero(self.caracter):
            self.siguienteEstado(5)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado06(self):
        if self.esComilla(self.caracter):
            self.siguienteEstado(7)
        elif self.esCaracter(self.caracter):
            self.siguienteEstado(6)
        else:
            self.retroceso()
    
    def estado07(self):
            self.retroceso()


    # Definimos todos los tipos validos

    def error(self):
        self.tipo = self.ERROR

    def tipo00(self):
        self.tipo = self.IDENTIFICADOR

    def tipo01(self):
        self.tipo = self.ENTERO
    
    def tipo02(self):
        self.tipo = self.REAL
    
    def tipo03(self):
        self.tipo = self.CADENA

    def tipo33(self):
        self.tipo = self.PESO

    
    # Definimos los mensajes de tipos
    
    def m_PESO(self):
        self.tipoCadenaMensaje = "Fin de Cadena"

    def m_ERROR(self):
        self.tipoCadenaMensaje = "No esta definido"
    
    def m_IDENTIFICADOR(self):
        self.tipoCadenaMensaje = "Identificador"

    def m_ENTERO(self):
        self.tipoCadenaMensaje = "Entero"

    def m_REAL(self):
        self.tipoCadenaMensaje = "Real"

    def m_CADENA(self):
        self.tipoCadenaMensaje = "Cadena"
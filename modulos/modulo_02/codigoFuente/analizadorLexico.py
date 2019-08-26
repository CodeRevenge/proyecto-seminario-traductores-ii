class TipoCadena:
    "Clase que define los tipos de simbolos"
    def __init__(self):
        self.ERROR = -2
        self.PESO = -1
        self.IDENTIFICADOR = 0
        self.ENTERO = 1
        self.REAL = 2
        self.CADENA = 3
        self.TIPO = 4
        self.OPSUMA = 5
        self.OPRESTA = 6
        self.OPMULTIPLICACION = 7
        self.OPDIVISION = 8
        self.OPOR = 9
        self.OPAND = 10
        self.OPNOT = 11
        self.OPMAYORQ = 12
        self.OPMENORQ = 13
        self.OPMAYOROIGUAL = 14
        self.OPMENOROIGUAL = 15
        self.OPIGUAL = 16
        self.OPESIGUAL = 17
        self.OPESDIFERENTE = 18
        self.PUNTOYCOMA = 19
        self.COMA = 20
        self.PARENTESIOSABIERTO = 21
        self.PARENTESISCERRADO = 22
        self.LLAVEABIERTA = 23
        self.LLAVECERRADA = 24
        self.BRACKETABIERTO = 25
        self.BRACKETCERRADO = 26
        self.DOSPUNTOS = 27
        self.IF = 50
        self.WHILE = 51 
        self.RETURN = 52
        self.ELSE = 53
        self.INT = 54
        self.FLOAT = 55
        self.VOID = 56
        

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
            self.OPSUMA: self.m_OPMAS,
            self.OPRESTA: self.m_OPMENOS,
            self.OPMULTIPLICACION: self.m_OPMULTI,
            self.OPDIVISION: self.m_OPDIV,
            self.OPMAYORQ: self.m_MAYORQUE,
            self.OPMENORQ: self.m_MENORQUE,
            self.OPMAYOROIGUAL: self.m_MAYORIGUAL,
            self.OPMENOROIGUAL: self.m_MENORIGUAL,
            self.OPOR: self.m_OR,
            self.OPAND: self.m_AND,
            self.OPNOT: self.m_NOT,
            self.OPIGUAL: self.m_IGUAL,
            self.OPESIGUAL: self.m_ESIGUAL,
            self.OPESDIFERENTE: self.m_ESDIFERENTE,
            self.PUNTOYCOMA: self.m_PUNTOCOMA,
            self.COMA: self.m_COMA,
            self.PARENTESIOSABIERTO: self.m_PARENTESISABIERTO,
            self.PARENTESISCERRADO: self.m_PARENTESISCERRADO,
            self.LLAVEABIERTA: self.m_LLAVEABIERTA,
            self.LLAVECERRADA: self.m_LLAVECERRADA,
            self.BRACKETABIERTO: self.m_BRACKETABIERTO,
            self.BRACKETCERRADO: self.m_BRACKETCERRADO,
            self.DOSPUNTOS: self.m_DOSPUNTOS,
            self.IF: self.m_IF,
            self.WHILE: self.m_WHILE,
            self.RETURN: self.m_RETURN,
            self.ELSE: self.m_ELSE,
            self.INT: self.m_INT,
            self.FLOAT: self.m_FLOAT,
            self.VOID: self.m_VOID,
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
                8: self.estado08,
                9: self.estado09,
                10: self.estado10,
                11: self.estado11,
                12: self.estado12,
                13: self.estado13,
                14: self.estado14,
                15: self.estado15,
                16: self.estado16,
                17: self.estado17,
                18: self.estado18,
                19: self.estado19,
                20: self.estado20,
                21: self.estado21,
                22: self.estado22,
                23: self.estado23,
                24: self.estado24,
                25: self.estado25,
                26: self.estado26,
                27: self.estado27,
                28: self.estado28,
                29: self.estado29,
                30: self.estado30,
                31: self.estado31,
                32: self.estado32
            }

            switch.get(self.estado, self.error)()

        # Terminamos el automata

        if self.tipo < 50:

            switch = {
                -2: self.error, # ERROR
                -1: self.tipoM1, # Peso
                2: self.tipo00, # Identificador
                3: self.tipo01, # Entero
                5: self.tipo02, # Real
                7: self.tipo03, # Cadena
                8: self.tipo05, # Suma
                9: self.tipo06, # Resta
                10: self.tipo07, # Multiplicacion
                11: self.tipo08, # Division
                17: self.tipo09, # OR
                19: self.tipo10, # AND
                20: self.tipo11, # NOT
                14: self.tipo12, # Mayor que
                12: self.tipo13, # Menor que
                15: self.tipo14, # Mayor o igual que
                13: self.tipo15, # Menor o igual que
                22: self.tipo16, # Igual
                23: self.tipo17, # Es igual
                21: self.tipo18, # Es diferente
                24: self.tipo19, # Punto y coma
                25: self.tipo20, # Coma
                26: self.tipo21, # Parantesis abierto
                27: self.tipo22, # Parentesis cerrado
                28: self.tipo23, # Llave abierta
                29: self.tipo24, # Llave cerrada
                30: self.tipo25, # Bracket abierto
                31: self.tipo26, # Bracket cerrado
                32: self.tipo27 # Dos puntos
            }

            switch.get(self.estado, self.error)()
        return (self.simbolo, self.tipo, self.tipoCadena(self.tipo))

    def verificarPalabraReservada(self, simbolo):
        palabrasReservadas = {
            "int": self.INT,
            "float": self.FLOAT,
            "void": self.VOID,
            "if": self.IF,
            "while": self.WHILE,
            "return": self.RETURN,
            "else": self.ELSE
        }
        self.tipo = palabrasReservadas.get(simbolo, self.tipo)

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
        self.verificarPalabraReservada(self.simbolo)

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

    def esMayorQue(self, caracter):
        return caracter == ">"

    def esMenorQue(self, caracter):
        return caracter == "<"

    def esPipe(self, caracter):
        return caracter == "|"

    def esAmpersand(self, caracter):
        return caracter == "&"

    def esFactorial(self, caracter):
        return caracter == "!"

    def esPuntoYComa(self, caracter):
        return caracter == ";"

    def esComa(self, caracter):
        return caracter == ","

    def esParentesisAbierto(self, caracter):
        return caracter == "("

    def esParentesisCerrado(self, caracter):
        return caracter == ")"

    def esLlaveAbierta(self, caracter):
        return caracter == "{"

    def esLlaveCerrada(self, caracter):
        return caracter == "}"

    def esBracketAbierto(self, caracter):
        return caracter == "["

    def esBracketCerrado(self, caracter):
        return caracter == "]"

    def esIgual(self, caracter):
        return caracter == "="

    def esDosPuntos(self, caracter):
        return caracter == ":"
    
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
        elif self.esSuma(self.caracter):
            self.siguienteEstado(8)
        elif self.esResta(self.caracter):
            self.siguienteEstado(9)
        elif self.esMultiplicacion(self.caracter):
            self.siguienteEstado(10)
        elif self.esDivision(self.caracter):
            self.siguienteEstado(11)
        elif self.esMenorQue(self.caracter):
            self.siguienteEstado(12)
        elif self.esMayorQue(self.caracter):
            self.siguienteEstado(14)
        elif self.esPipe(self.caracter):
            self.siguienteEstado(16)
        elif self.esAmpersand(self.caracter):
            self.siguienteEstado(18)
        elif self.esFactorial(self.caracter):
            self.siguienteEstado(20)
        elif self.esIgual(self.caracter):
            self.siguienteEstado(22)
        elif self.esPuntoYComa(self.caracter):
            self.siguienteEstado(24)
        elif self.esComa(self.caracter):
            self.siguienteEstado(25)
        elif self.esParentesisAbierto(self.caracter):
            self.siguienteEstado(26)
        elif self.esParentesisCerrado(self.caracter):
            self.siguienteEstado(27)
        elif self.esLlaveAbierta(self.caracter):
            self.siguienteEstado(28)
        elif self.esLlaveCerrada(self.caracter):
            self.siguienteEstado(29)
        elif self.esBracketAbierto(self.caracter):
            self.siguienteEstado(30)
        elif self.esBracketCerrado(self.caracter):
            self.siguienteEstado(31)
        elif self.esDosPuntos(self.caracter):
            self.siguienteEstado(32)
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
            self.verificarPalabraReservada(self.simbolo)
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

    def estado08(self):
        self.retroceso()

    def estado09(self):
        self.retroceso()

    def estado10(self):
        self.retroceso()

    def estado11(self):
        self.retroceso()

    def estado12(self):
        if self.esIgual(self.caracter):
            self.siguienteEstado(13)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado13(self):
        self.retroceso()

    def estado14(self):
        if self.esIgual(self.caracter):
            self.siguienteEstado(15)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado15(self):
        self.retroceso()

    def estado16(self):
        if self.esPipe(self.caracter):
            self.siguienteEstado(17)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado17(self):
        self.retroceso()

    def estado18(self):
        if self.esAmpersand(self.caracter):
            self.siguienteEstado(19)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado19(self):
        self.retroceso()

    def estado20(self):
        if self.esIgual(self.caracter):
            self.siguienteEstado(21)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado21(self):
        self.retroceso()

    def estado22(self):
        if self.esIgual(self.caracter):
            self.siguienteEstado(23)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.retroceso()

    def estado23(self):
        self.retroceso()

    def estado24(self):
        self.retroceso()

    def estado25(self):
        self.retroceso()

    def estado26(self):
        self.retroceso()

    def estado27(self):
        self.retroceso()

    def estado28(self):
        self.retroceso()

    def estado29(self):
        self.retroceso()

    def estado30(self):
        self.retroceso()

    def estado31(self):
        self.retroceso()

    def estado32(self):
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

    def tipo04(self):
        self.tipo = self.TIPO

    def tipo05(self):
        self.tipo = self.OPSUMA

    def tipo06(self):
        self.tipo = self.OPRESTA

    def tipo07(self):
        self.tipo = self.OPMULTIPLICACION

    def tipo08(self):
        self.tipo = self.OPDIVISION

    def tipo09(self):
        self.tipo = self.OPOR

    def tipo10(self):
        self.tipo = self.OPAND

    def tipo11(self):
        self.tipo = self.OPNOT

    def tipo12(self):
        self.tipo = self.OPMAYORQ

    def tipo13(self):
        self.tipo = self.OPMENORQ

    def tipo14(self):
        self.tipo = self.OPMAYOROIGUAL

    def tipo15(self):
        self.tipo = self.OPMENOROIGUAL

    def tipo16(self):
        self.tipo = self.OPIGUAL

    def tipo17(self):
        self.tipo = self.OPESIGUAL

    def tipo18(self):
        self.tipo = self.OPESDIFERENTE

    def tipo19(self):
        self.tipo = self.PUNTOYCOMA

    def tipo20(self):
        self.tipo = self.COMA

    def tipo21(self):
        self.tipo = self.PARENTESIOSABIERTO

    def tipo22(self):
        self.tipo = self.PARENTESISCERRADO

    def tipo23(self):
        self.tipo = self.LLAVEABIERTA

    def tipo24(self):
        self.tipo = self.LLAVECERRADA

    def tipo25(self):
        self.tipo = self.BRACKETABIERTO

    def tipo26(self):
        self.tipo = self.BRACKETCERRADO

    def tipo27(self):
        self.tipo = self.DOSPUNTOS
    
    def tipoM1(self):
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

    def m_OPMAS(self):
        self.tipoCadenaMensaje = "Mas"

    def m_OPMENOS(self):
        self.tipoCadenaMensaje = "Menos"

    def m_OPMULTI(self):
        self.tipoCadenaMensaje = "Multiplicacion"

    def m_OPDIV(self):
        self.tipoCadenaMensaje = "Division"

    def m_MAYORQUE(self):
        self.tipoCadenaMensaje = "Mayor que"

    def m_MENORQUE(self):
        self.tipoCadenaMensaje = "Menor que"

    def m_MAYORIGUAL(self):
        self.tipoCadenaMensaje = "Mayor o igual que"

    def m_MENORIGUAL(self):
        self.tipoCadenaMensaje = "Menor o igual que"

    def m_OR(self):
        self.tipoCadenaMensaje = "Or"

    def m_AND(self):
        self.tipoCadenaMensaje = "And"

    def m_NOT(self):
        self.tipoCadenaMensaje = "Not"

    def m_IGUAL(self):
        self.tipoCadenaMensaje = "Igual"

    def m_ESIGUAL(self):
        self.tipoCadenaMensaje = "Es igual a"

    def m_ESDIFERENTE(self):
        self.tipoCadenaMensaje = "Es diferente de"

    def m_PUNTOCOMA(self):
        self.tipoCadenaMensaje = "Punto y coma"

    def m_COMA(self):
        self.tipoCadenaMensaje = "Coma"

    def m_PARENTESISABIERTO(self):
        self.tipoCadenaMensaje = "Parentesis abierto"

    def m_PARENTESISCERRADO(self):
        self.tipoCadenaMensaje = "Parentesis abierto"

    def m_LLAVEABIERTA(self):
        self.tipoCadenaMensaje = "Llave abierta"

    def m_LLAVECERRADA(self):
        self.tipoCadenaMensaje = "Llave cerrada"

    def m_BRACKETABIERTO(self):
        self.tipoCadenaMensaje = "Bracket abierto"

    def m_BRACKETCERRADO(self):
        self.tipoCadenaMensaje = "Bracket cerrado"

    def m_DOSPUNTOS(self):
        self.tipoCadenaMensaje = "Dos puntos"

    def m_IF(self):
        self.tipoCadenaMensaje = "If"

    def m_WHILE(self):
        self.tipoCadenaMensaje = "While"

    def m_RETURN(self):
        self.tipoCadenaMensaje = "Return"

    def m_ELSE(self):
        self.tipoCadenaMensaje = "Else"

    def m_INT(self):
        self.tipoCadenaMensaje = "Int"

    def m_FLOAT(self):
        self.tipoCadenaMensaje = "Float"

    def m_VOID(self):
        self.tipoCadenaMensaje = "Void"
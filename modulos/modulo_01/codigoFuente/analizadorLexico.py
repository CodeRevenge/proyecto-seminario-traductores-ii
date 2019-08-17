class TipoCadena:
    "Clase que define los tipos de simbolos"
    def __init__(self):
        self.ERROR = -1
        self.IDENTIFICADOR = 0
        self.ENTERO = 1
        self.REAL = 2

class Estados:
    "Clase que define los metodos de cada estado"
    def __init__(self, caracter):
        self.caracter = caracter

    

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
            self.REAL: self.m_REAL
        }

        switch[tipo]()

        return self.tipoCadenaMensaje

        

    def siguienteSimbolo(self):
        self.estado = 1
        self.continua = True
        self.simbolo = ""
        self.tipo = -1

        # Damos inicio al automata
        
        # Mientras la cadena no llegue a un espacio continua
        while self.continua:
            # Seleccionamos el siguiente caracter de la cadena
            self.caracter = self.siguienteCaracter()

            if(self.caracter == "$"):
                break

            switch = {
                1: self.estado01,
                2: self.estado02,
                3: self.estado03,
                4: self.estado04,
                5: self.estado05
            }

            switch.get(self.estado, self.error)()

        # Terminamos el automata

        switch = {
            -1: self.error,
            2: self.tipo00,
            3: self.tipo01,
            5: self.tipo02
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

    # Definimos funciones que evaluan el tipo de caracter

    def esLetra(self, caracter):
        "Regresa True si el caracter es una letra o un guion bajo y False si no lo es"
        return caracter.isalpha() or caracter == "_"

    def esNumero(self, caracter):
        "Regresa True si el caracter es un numero y False si no lo es"
        return caracter.isdigit()

    def esPunto(self, caracter):
        "Regresa True si el caracter es un punto y False si no lo es"
        return caracter == "."
    
    def esEspacio(self, caracter):
        "Regresa True si el caracter es un espacio y False si no lo es"
        return caracter == " "

    def retroceso(self):
        
        if self.caracter != "$":
            self.indice -= 1
        self.continua = False
    
    def encontrarEspacio(self):
        self.continua = False
        self.estado = -1
        if self.terminado():
            self.caracter = "$"
            return

        for x in range(self.indice, len(self.cadena)):
            self.simbolo += self.caracter + self.cadena[x]
            self.caracter = ""
            if self.esEspacio(self.cadena[x]):
                self.indice = x+1
                break

    def terminado(self):
        return self.indice >= len(self.cadena)
    
    # Definimos todos los estados

    def estado01(self):
        if self.esLetra(self.caracter):
            self.siguienteEstado(2)
        elif self.esNumero(self.caracter):
            self.siguienteEstado(3)
        elif self.esEspacio(self.caracter):
            self.siguienteEstado(1)
        else:
            self.encontrarEspacio()

    def estado02(self):
        if self.esLetra(self.caracter):
            self.siguienteEstado(2)
        elif self.esNumero(self.caracter):
            self.siguienteEstado(2)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.encontrarEspacio()

    def estado03(self):
        if self.esNumero(self.caracter):
            self.siguienteEstado(3)
        elif self.esPunto(self.caracter):
            self.tipo = -1
            self.siguienteEstado(4)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.encontrarEspacio()

    def estado04(self):
        if self.esNumero(self.caracter):
            self.siguienteEstado(5)
        else:
            self.encontrarEspacio()

    def estado05(self):
        if self.esNumero(self.caracter):
            self.siguienteEstado(5)
        elif self.esEspacio(self.caracter):
            self.continua = False
        else:
            self.encontrarEspacio()

    # Definimos todos los tipos validos

    def error(self):
        self.tipo = self.ERROR

    def tipo00(self):
        self.tipo = self.IDENTIFICADOR

    def tipo01(self):
        self.tipo = self.ENTERO
    
    def tipo02(self):
        self.tipo = self.REAL

    
    # Definimos los mensajes de tipos
    
    def m_ERROR(self):
        self.tipoCadenaMensaje = "No esta definido"
    
    def m_IDENTIFICADOR(self):
        self.tipoCadenaMensaje = "Identificador"

    def m_ENTERO(self):
        self.tipoCadenaMensaje = "Entero"

    def m_REAL(self):
        self.tipoCadenaMensaje = "Real"
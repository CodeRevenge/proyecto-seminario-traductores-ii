class Reglas:
    def __init__(self):
        self.IDENTIFICADOR = 0
        self.ENTERO = 1
        self.REAL = 2
        self.CADENA = 3
        self.TIPO = 4
        self.OPSUMA = 5
        self.OPMUL = 6
        self.OPRELAC = 7
        self.OPOR = 8
        self.OPAND = 9
        self.OPNOT = 10
        self.OPIGUALDAD = 11
        self.PUNTOYCOMA = 12
        self.COMA = 13
        self.PARENTESISABIERTO = 14
        self.PARENTESISCERRADO = 15
        self.LLAVEABIERTA = 16
        self.LLAVECERRADA = 17
        self.IGUAL = 18
        self.IF_ = 19
        self.WHILE_ = 20
        self.RETURN_ = 21
        self.ELSE_ = 22
        self.PESO = 23
        self.PROGRAMA = 24
        self.DEFINICIONES = 25
        self.DEFINICION = 26
        self.DEFVAR = 27
        self.LISTAVAR = 28
        self.DEFFUNC = 29
        self.PARAMETROS = 30
        self.LISTAPARAM = 31
        self.BLOQFUNC = 32
        self.DEFLOCALES = 33
        self.DEFLOCAL = 34
        self.SENTENCIAS = 35
        self.SENTENCIA = 36
        self.OTRO = 37
        self.BLOQUE = 38
        self.VALORREGRESA = 39
        self.ARGUMENTOS = 40
        self.LISTAARGUMENTOS = 41
        self.TERMINO = 42
        self.LLAMADAFUNC = 43
        self.SENTENCIABLOQUE = 44
        self.EXPRESION = 45


class Nodo:
    def __init__(self):
        pass

class Programa(Nodo):
    def __init__(self, Definiciones):
        Nodo.__init__(self)
        self.definiciones = Definiciones

    def muestra(self):
        if self.definiciones:
            self.definiciones.muestra()

class Definiciones(Nodo):
    def __init__(self, Definicion, Definiciones):
        Nodo.__init__(self)
        self.definicion = Definicion
        self.definiciones = Definiciones

    def muestra(self):
        if self.definicion:
            self.definicion.muestra()
        if self.definiciones:
            self.definiciones.muestra()

class DefinicionVar(Nodo):
    def __init__(self, DefVar):
        Nodo.__init__(self)
        self.defvar = DefVar

    def muestra(self):
        if self.defvar:
            self.defvar.muestra()

class DefinicionFunc(Nodo):
    def __init__(self, DefFunc):
        Nodo.__init__(self)
        self.defFunc = DefFunc

    def muestra(self):
        if self.defFunc:
            self.defFunc.muestra()

class DefVar(Nodo):
    def __init__(self, tipo, identificador, ListaVar):
        Nodo.__init__(self)
        self.tipo = tipo
        self.identificador = identificador
        self.listaVar = ListaVar

    def muestra(self):
        print(self.tipo)
        print(self.identificador)
        if self.listaVar:
            self.listaVar.muestra()

class ListaVar(Nodo):
    def __init__(self, identificador, ListaVar):
        Nodo.__init__(self)
        self.identificador = identificador
        self.listaVar = ListaVar

    def muestra(self):
        print(self.identificador)
        if self.listaVar:
            self.listaVar.muestra()

class DefFunc(Nodo):
    def __init__(self, tipo, identificador, Parametros, BloqFunc):
        Nodo.__init__(self)
        self.tipo = tipo
        self.identificador = identificador
        self.Parametros = Parametros
        self.BloqFunc = BloqFunc

    def muestra(self):
        print(self.tipo)
        print(self.identificador)
        if self.Parametros:
            self.Parametros.muestra()
        if self.BloqFunc:
            self.BloqFunc.muestra()

class Parametros(Nodo):
    def __init__(self, tipo, identificador, ListaParam):
        Nodo.__init__(self)
        self.tipo = tipo
        self.identificador = identificador
        self.ListaParam = ListaParam

    def muestra(self):
        print(self.tipo)
        print(self.identificador)
        if self.ListaParam:
            self.ListaParam.muestra()

class ListaParam(Nodo):
    def __init__(self, tipo, identificador, ListaParam):
        Nodo.__init__(self)
        self.tipo = tipo
        self.identificador = identificador
        self.ListaParam = ListaParam

    def muestra(self):
        print(self.tipo)
        print(self.identificador)
        if self.ListaParam:
            self.ListaParam.muestra()

class BloqFunc(Nodo):
    def __init__(self, DefLocales):
        Nodo.__init__(self)
        self.DefLocales = DefLocales

    def muestra(self):
        if self.DefLocales:
            self.DefLocales.muestra()

class DefLocales(Nodo):
    def __init__(self, DefLocal, DefLocales):
        Nodo.__init__(self)
        self.DefLocal = DefLocal
        self.DefLocales = DefLocales

    def muestra(self):
        if self.DefLocal:
            self.DefLocal.muestra()
        if self.DefLocales:
            self.DefLocales.muestra()

class DefLocalVar(Nodo):
    def __init__(self, DefVar):
        Nodo.__init__(self)
        self.DefVar = DefVar

    def muestra(self):
        if self.DefVar:
            self.DefVar.muestra()

class DefLocalSent(Nodo):
    def __init__(self, Sentencia):
        Nodo.__init__(self)
        self.Sentencia = Sentencia

    def muestra(self):
        if self.Sentencia:
            self.Sentencia.muestra()

class Sentencias(Nodo):
    def __init__(self, Sentencia, Sentencias):
        Nodo.__init__(self)
        self.Sentencia = Sentencia
        self.Sentencias = Sentencias

    def muestra(self):
        if self.Sentencia:
            self.Sentencia.muestra()
        if self.Sentencias:
            self.Sentencias.muestra()

class SentenciaExpre(Nodo):
    def __init__(self, identificador, Expresion):
        Nodo.__init__(self)
        self.identificador = identificador
        self.Expresion = Expresion

    def muestra(self):
        print(self.identificador)
        if self.Expresion:
            self.Expresion.muestra()

class SentenciaIf(Nodo):
    def __init__(self, Expresion, Sentencia, Otro):
        Nodo.__init__(self)
        self.Expresion = Expresion
        self.Sentencia = Sentencia
        self.Otro = Otro

    def muestra(self):
        if self.Expresion:
            self.Expresion.muestra()
        if self.Sentencia:
            self.Sentencia.muestra()
        if self.Otro:
            self.Otro.muestra()

class SentenciaWhile(Nodo):
    def __init__(self, Expresion, Bloque):
        Nodo.__init__(self)
        self.Expresion = Expresion
        self.Bloque = Bloque

    def muestra(self):
        if self.Expresion:
            self.Expresion.muestra()
        if self.Bloque:
            self.Bloque.muestra()

class SentenciaReturn(Nodo):
    def __init__(self, ValorRegresa):
        Nodo.__init__(self)
        self.ValorRegresa = ValorRegresa

    def muestra(self):
        if self.ValorRegresa:
            self.ValorRegresa.muestra()

class SentenciaFunc(Nodo):
    def __init__(self, LlamadaFunc):
        Nodo.__init__(self)
        self.LlamadaFunc = LlamadaFunc

    def muestra(self):
        if self.LlamadaFunc:
            self.LlamadaFunc.muestra()

class Otro(Nodo):
    def __init__(self, SentenciaBloque):
        Nodo.__init__(self)
        self.SentenciaBloque = SentenciaBloque

    def muestra(self):
        if self.SentenciaBloque:
            self.SentenciaBloque.muestra()

class Bloque(Nodo):
    def __init__(self, Sentencias):
        Nodo.__init__(self)
        self.Sentencias = Sentencias

    def muestra(self):
        if self.Sentencias:
            self.Sentencias.muestra()

class ValorRegresa(Nodo):
    def __init__(self, Expresion):
        Nodo.__init__(self)
        self.Expresion = Expresion

    def muestra(self):
        if self.Expresion:
            self.Expresion.muestra()

class Argumentos(Nodo):
    def __init__(self, Expresion, ListaArgumentos):
        Nodo.__init__(self)
        self.Expresion = Expresion
        self.ListaArgumentos = ListaArgumentos

    def muestra(self):
        if self.Expresion:
            self.Expresion.muestra()
        if self.ListaArgumentos:
            self.ListaArgumentos.muestra()

class ListaArgumentos(Nodo):
    def __init__(self, Expresion, ListaArgumentos):
        Nodo.__init__(self)
        self.Expresion = Expresion
        self.ListaArgumentos = ListaArgumentos

    def muestra(self):
        if self.Expresion:
            self.Expresion.muestra()
        if self.ListaArgumentos:
            self.ListaArgumentos.muestra()

class TerminoFunc(Nodo):
    def __init__(self, LlamadaFunc):
        Nodo.__init__(self)
        self.LlamadaFunc = LlamadaFunc

    def muestra(self):
        if self.LlamadaFunc:
            self.LlamadaFunc.muestra()

class TerminoIdent(Nodo):
    def __init__(self, identificador):
        Nodo.__init__(self)
        self.identificador = identificador

    def muestra(self):
        print(self.identificador)

class TerminoEntero(Nodo):
    def __init__(self, entero):
        Nodo.__init__(self)
        self.entero = entero

    def muestra(self):
        print(self.entero)

class TerminoReal(Nodo):
    def __init__(self, real):
        Nodo.__init__(self)
        self.real = real

    def muestra(self):
        print(self.real)

class TerminoCadena(Nodo):
    def __init__(self, cadena):
        Nodo.__init__(self)
        self.cadena = cadena

    def muestra(self):
        print(self.cadena)

class LlamadaFunc(Nodo):
    def __init__(self, identificador, Argumentos):
        Nodo.__init__(self)
        self.identificador = identificador
        self.Argumentos = Argumentos

    def muestra(self):
        print(self.identificador)
        if self.Argumentos:
            self.Argumentos.muestra()

class SentenciaBloque(Nodo):
    def __init__(self, Sentencia):
        Nodo.__init__(self)
        self.Sentencia = Sentencia

    def muestra(self):
        if self.Sentencia:
            self.Sentencia.muestra()

class Expresion(Nodo):
    def __init__(self, Expresion):
        Nodo.__init__(self)
        self.Expresion = Expresion

    def muestra(self):
        if self.Expresion:
            self.Expresion.muestra()

class ExpresionSuma(Nodo):
    def __init__(self, Expresion):
        Nodo.__init__(self)
        self.Expresion = Expresion

    def muestra(self):
        if self.Expresion:
            self.Expresion.muestra()

class ExpresionNot(Nodo):
    def __init__(self, Expresion):
        Nodo.__init__(self)
        self.Expresion = Expresion

    def muestra(self):
        if self.Expresion:
            self.Expresion.muestra()

class ExpresionOp(Nodo):
    def __init__(self, ExpresionUno, ExpresionDos):
        Nodo.__init__(self)
        self.ExpresionUno = ExpresionUno
        self.ExpresionDos = ExpresionDos

    def muestra(self):
        if self.ExpresionUno:
            self.ExpresionUno.muestra()
        if self.ExpresionDos:
            self.ExpresionDos.muestra()

class ExpresionTermino(Nodo):
    def __init__(self, Termino):
        Nodo.__init__(self)
        self.Termino = Termino

    def muestra(self):
        if self.Termino:
            self.Termino.muestra()

class Arbol(Reglas):
    def __init__(self):
        Reglas.__init__(self)
        self.arbol = []
    
    def insertarNodo(self, tipo, entero, simbolos):
        if entero == self.PROGRAMA:
            programa = Programa(self.arbol.pop())
            self.arbol = programa
        elif entero == self.DEFINICIONES:
            if simbolos:
                definiciones = Definiciones(self.arbol.pop(-2), self.arbol.pop())
                self.arbol.append(definiciones)
            else:
                definiciones = Definiciones(None, None)
                self.arbol.append(definiciones)
        elif entero == self.DEFINICION:
            if simbolos[0] == 'DefVar':
                definicion = DefinicionVar(self.arbol.pop())
                self.arbol.append(definicion)
            elif simbolos[0] == 'DefFunc':
                definicion = DefinicionFunc(self.arbol.pop())
                self.arbol.append(definicion)
        elif entero == self.DEFVAR:
            defvar = DefVar(simbolos[3], simbolos[2], self.arbol.pop())
            self.arbol.append(defvar)
        elif entero == self.LISTAVAR:
            if simbolos:
                listavar = ListaVar(simbolos[2],self.arbol.pop())
                self.arbol.append(listavar)
            else:
                listavar = ListaVar(None, None)
                self.arbol.append(listavar)
        elif entero == self.DEFFUNC:
            deffunc = DefFunc(simbolos[5], simbolos[4], self.arbol.pop(-2), self.arbol.pop())
            self.arbol.append(deffunc)
        elif entero == self.PARAMETROS:
            if simbolos:
                parametros = Parametros(simbolos[2],simbolos[1],self.arbol.pop())
                self.arbol.append(parametros)
            else:
                parametros = Parametros(None, None, None)
                self.arbol.append(parametros)
        elif entero == self.LISTAPARAM:
            if simbolos:
                listaParam = ListaParam(simbolos[2], simbolos[1], self.arbol.pop())
                self.arbol.append(listaParam)
            else:
                listaParam = ListaParam(None, None, None)
                self.arbol.append(listaParam)
        elif entero == self.BLOQFUNC:
            bloqfunc = BloqFunc(self.arbol.pop())
            self.arbol.append(bloqfunc)
        elif entero == self.DEFLOCALES:
            if simbolos:
                deflocal = DefLocales(self.arbol.pop(-2), self.arbol.pop())
                self.arbol.append(deflocal)
            else:
                deflocal = DefLocales(None, None)
                self.arbol.append(deflocal)
        elif entero == self.DEFLOCAL:
            if simbolos[0] == 'DefVar':
                deflocal = DefLocalVar(self.arbol.pop())
                self.arbol.append(deflocal)
            elif simbolos[0] == 'Sentencia':
                deflocal = DefLocalSent(self.arbol.pop())
                self.arbol.append(deflocal)
        elif entero == self.SENTENCIAS:
            if simbolos:
                sentencia = Sentencias(self.arbol.pop(-2), self.arbol.pop())
                self.arbol.append(sentencia)
            else:
                sentencia = Sentencias(None, None)
                self.arbol.append(sentencia)
        elif entero == self.SENTENCIA:
            if tipo == 'SentenciaIdent':
                sentencia = SentenciaExpre(simbolos[-1],self.arbol.pop())
                self.arbol.append(sentencia)
            elif tipo == 'SentenciaIf':
                sentencia = SentenciaIf(self.arbol.pop(-3), self.arbol.pop(-2),self.arbol.pop())
                self.arbol.append(sentencia)
            elif tipo == 'SentenciaWhile':
                sentencia = SentenciaWhile(self.arbol.pop(-2),self.arbol.pop())
                self.arbol.append(sentencia)
            elif tipo == 'SentenciaReturn':
                sentencia = SentenciaReturn(self.arbol.pop())
                self.arbol.append(sentencia)
            elif tipo == 'SentenciaLlamada':
                sentencia = SentenciaFunc(self.arbol.pop())
                self.arbol.append(sentencia)
        elif entero == self.OTRO:
            if simbolos:
                otro = Otro(self.arbol.pop())
                self.arbol.append(otro)
            else:
                otro = Otro(None)
                self.arbol.append(otro)
        elif entero == self.BLOQUE:
            bloque = Bloque(self.arbol.pop())
            self.arbol.append(bloque)
        elif entero == self.VALORREGRESA:
            if simbolos:
                regresa = ValorRegresa(self.arbol.pop())
                self.arbol.append(regresa)
            else:
                regresa = ValorRegresa(None)
                self.arbol.append(regresa)
        elif entero == self.ARGUMENTOS:
            if simbolos:
                argumento = Argumentos(self.arbol.pop(-2), self.arbol.pop())
                self.arbol.append(argumento)
            else:
                argumento = Argumentos(None, None)
                self.arbol.append(argumento)
        elif entero == self.LISTAARGUMENTOS:
            if simbolos:
                argumentos = ListaArgumentos(self.arbol.pop(-2), self.arbol.pop())
                self.arbol.append(argumentos)
            else:
                argumentos = ListaArgumentos(None, None)
                self.arbol.append(argumentos)
        elif entero == self.TERMINO:
            if tipo == 'TerminoLlamada':
                termino = TerminoIdent(self.arbol.pop())
                self.arbol.append(termino)
            elif tipo == 'TerminoIdent':
                termino = TerminoIdent(simbolos[-1])
                self.arbol.append(termino)
            elif tipo == 'TerminoEntero':
                termino = TerminoEntero(int(simbolos[-1]))
                self.arbol.append(termino)
            elif tipo == 'TerminoReal':
                termino = TerminoReal(float(simbolos[-1]))
                self.arbol.append(termino)
            elif tipo == 'TerminoCadena':
                termino = TerminoCadena(simbolos[-1])
                self.arbol.append(termino)
        elif entero == self.LLAMADAFUNC:
            llamada = LlamadaFunc(simbolos[0], self.arbol.pop())
            self.arbol.append(llamada)
        elif entero == self.SENTENCIABLOQUE:
            if simbolos[-1] == 'Sentencia':
                sentencia = SentenciaBloque(self.arbol.pop())
                self.arbol.append(sentencia)
            elif simbolos[-1] == 'Bloque':
                sentencia = Bloque(self.arbol.pop())
                self.arbol.append(sentencia)
        elif entero == self.EXPRESION:
            if tipo == 'Expresion':
                expresion = Expresion(self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionSuma':
                expresion = ExpresionSuma(self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionNot':
                expresion = ExpresionNot(self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionMul':
                expresion = ExpresionOp(self.arbol.pop(-2),self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionSumaDos':
                expresion = ExpresionOp(self.arbol.pop(-2),self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionRelac':
                expresion = ExpresionOp(self.arbol.pop(-2),self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionIgualdad':
                expresion = ExpresionOp(self.arbol.pop(-2),self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionAnd':
                expresion = ExpresionOp(self.arbol.pop(-2),self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionOr':
                expresion = ExpresionOp(self.arbol.pop(-2),self.arbol.pop())
                self.arbol.append(expresion)
            if tipo == 'ExpresionTerm':
                expresion = ExpresionTermino(self.arbol.pop())
                self.arbol.append(expresion)
import sys
sys.tracebacklimit = 0

class AnalizadorSemantico:
    def __init__(self, arbol):
        self.arbol = arbol
        # [identificador, tipo, ambito, esFuncion]
        self.tabla_simbolos = []
        self.call_stack = ['Global']

        self.recorrer_arbol(self.arbol)

    def existe_simbolo(self, identificador, tipo= None, ambito = 'Global', esFuncion = False):
        if tipo:
            for item in self.tabla_simbolos:
                if identificador == item[0]:
                    if tipo == item[1]:
                        if ambito == item[2]:
                            if esFuncion == item[3]:
                                return True
            return False
        else:
            for item in self.tabla_simbolos:
                if identificador == item[0]:
                    return True
            return False


    def recorrer_arbol(self, arbol, *args):
        if arbol is not None:
            if str(type(arbol)) != '<class \'str\'>':
                clase = str(type(arbol)).split('.')[2].rstrip('\'>')
                if clase == 'Programa':
                    self.recorrer_arbol(arbol.definiciones)
                elif clase == 'Definiciones':
                    self.recorrer_arbol(arbol.definicion)
                    self.recorrer_arbol(arbol.definiciones)
                elif clase == 'DefinicionVar':
                    self.recorrer_arbol(arbol.defvar)
                elif clase == 'DefinicionFunc':
                    self.recorrer_arbol(arbol.defFunc)
                elif clase == 'DefVar':
                    if arbol.identificador is not None:
                        if not self.existe_simbolo(arbol.identificador, arbol.tipo, self.call_stack[-1]):
                            self.tabla_simbolos.append([arbol.identificador, arbol.tipo, self.call_stack[-1], False])
                        else:
                            raise Exception('La variable {} -> {} esta definida anteriormente'.format(arbol.tipo, arbol.identificador))
                        self.recorrer_arbol(arbol.listaVar, arbol.tipo)
                elif clase == 'ListaVar':
                    if arbol.identificador is not None:
                        if not self.existe_simbolo(arbol.identificador, args[0], self.call_stack[-1]):
                            self.tabla_simbolos.append([arbol.identificador, args[0], self.call_stack[-1], False])
                        else:
                            raise Exception('La variable {} -> {} esta definida anteriormente'.format(args[0], arbol.identificador))
                        self.recorrer_arbol(arbol.listaVar, args[0])
                elif clase == 'DefFunc':
                    if arbol.identificador is not None:
                        if not self.existe_simbolo(arbol.identificador, arbol.tipo, self.call_stack[-1]):
                            self.tabla_simbolos.append([arbol.identificador, arbol.tipo, self.call_stack[-1], True])
                            self.call_stack.append(arbol.identificador)
                        else:
                            raise Exception('El nombre {} ya esta definido anteriormente'.format(arbol.identificador))
                        self.recorrer_arbol(arbol.Parametros)
                        self.recorrer_arbol(arbol.BloqFunc)
                        self.call_stack.pop()
                elif clase == 'Parametros':
                    if arbol.tipo is not None:
                        self.tabla_simbolos.append([arbol.identificador, arbol.tipo, self.call_stack[-1], False])
                        self.recorrer_arbol(arbol.ListaParam)
                elif clase == 'ListaParam':
                    if arbol.tipo is not None:
                        if not self.existe_simbolo(arbol.identificador, arbol.tipo, self.call_stack[-1]):
                            self.tabla_simbolos.append([arbol.identificador, arbol.tipo, self.call_stack[-1], False])
                            self.call_stack.append(arbol.identificador)
                        else:
                            raise Exception('El parametro {} ya esta definido anteriormente'.format(arbol.identificador))
                        self.recorrer_arbol(arbol.ListaParam)
                elif clase == 'BloqFunc':
                    self.recorrer_arbol(arbol.DefLocales)
                elif clase == 'DefLocales':
                    if arbol.DefLocal is not None:
                        self.recorrer_arbol(arbol.DefLocal)
                        self.recorrer_arbol(arbol.DefLocales)
                elif clase == 'DefLocalVar':
                    self.recorrer_arbol(arbol.DefVar)
                elif clase == 'DefLocalSent':
                    self.recorrer_arbol(arbol.Sentencia)
                elif clase == 'Sentencias':
                    if arbol.Sentencia is not None:
                        self.recorrer_arbol(arbol.Sentencia)
                        self.recorrer_arbol(arbol.Sentencias)
                elif clase == 'SentenciaExpre':
                    cs = self.call_stack.copy()
                    cs.reverse()
                    for ambito in cs:
                        if self.existe_simbolo(arbol.identificador, ambito=ambito):
                            self.recorrer_arbol(arbol.Expresion)
                            break
                    else:
                        raise Exception('El identificador {} no esta definido'.format(arbol.identificador))
                elif clase == 'SentenciaIf':
                    self.recorrer_arbol(arbol.Expresion)
                    self.call_stack.append('If')
                    self.recorrer_arbol(arbol.Sentencia)
                    self.call_stack.pop()
                    self.call_stack.append('Else')
                    self.recorrer_arbol(arbol.Otro)
                    self.call_stack.pop()
                elif clase == 'SentenciaWhile':
                    self.recorrer_arbol(arbol.Expresion)
                    self.call_stack.append('While')
                    self.recorrer_arbol(arbol.Bloque)
                    self.call_stack.pop()
                elif clase == 'SentenciaReturn':
                    self.recorrer_arbol(arbol.ValorRegresa)
                elif clase == 'SentenciaFunc':
                    self.recorrer_arbol(arbol.LlamadaFunc)
                elif clase == 'Otro':
                    if arbol.SentenciaBloque is not None:
                        self.recorrer_arbol(arbol.SentenciaBloque)
                elif clase == 'Bloque':
                    self.recorrer_arbol(arbol.Sentencias)
                elif clase == 'ValorRegresa':
                    if arbol.Expresion is not None:
                        self.recorrer_arbol(arbol.Expresion)
                elif clase == 'Arbumentos':
                    if arbol.Expresion is not None:
                        self.recorrer_arbol(arbol.Expresion)
                        self.recorrer_arbol(arbol.ListaArgumentos)
                elif clase == 'ListaArgumentos':
                    if arbol.Expresion is not None:
                        self.recorrer_arbol(arbol.Expresion)
                        self.recorrer_arbol(arbol.ListaArgumentos)
                elif clase == 'TerminoFunc':
                    self.recorrer_arbol(arbol.LlamadaFunc)
                elif clase == 'TerminoIdent':
                    cs = self.call_stack.copy()
                    cs.reverse()
                    for ambito in cs:
                        if self.existe_simbolo(arbol.identificador, ambito=ambito):
                            break
                    else:
                        raise Exception('El identificador {} no esta definido'.format(arbol.identificador))
                elif clase == 'TerminoEntero':
                    return
                elif clase == 'TerminoReal':
                    return
                elif clase == 'TerminoCadena':
                    return
                elif clase == 'LlamadaFunc':
                    cs = self.call_stack.copy()
                    cs.reverse()
                    for ambito in cs:
                        if self.existe_simbolo(arbol.identificador, ambito=ambito, esFuncion= True):
                            self.recorrer_arbol(arbol.Argumentos)
                            break
                    else:
                        raise Exception('La función {} no esta definido'.format(arbol.identificador))
                elif clase == 'SentenciaBloque':
                    self.recorrer_arbol(arbol.Sentencia)
                elif clase == 'Expresion':
                    self.recorrer_arbol(arbol.Expresion)
                elif clase == 'ExpresionSuma':
                    self.recorrer_arbol(arbol.Expresion)
                elif clase == 'ExpresionNot':
                    self.recorrer_arbol(arbol.Expresion)
                elif clase == 'ExpresionOp':
                    self.recorrer_arbol(arbol.ExpresionUno)
                    self.recorrer_arbol(arbol.ExpresionDos)
                elif clase == 'ExpresionTermino':
                    self.recorrer_arbol(arbol.Termino)

                



                        


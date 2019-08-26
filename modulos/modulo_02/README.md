# Módulo 2: Ejemplos LR(1)

Utilizando el autómata del módulo 1, se implementara un analizador sintáctico utilizando la tabla **LR(1)** para diferentes gramaticas

## Gramaticas

+ `E → id + E | id`

## Especificaciones de módulo

[Aquí](/modulos/modulo_02/EjemplosPractica2.pdf) se encuentran las especificaciones minimas para este módulo proporcionadas por el Ingeniero Michel Emanuel López Franco

## Ejercicio a realizar

Del documento [EjemploPractica2.pdf](/modulos/modulo_02/EjemplosPractica2.pdf) se realizara el ejercicio 1 de la segunda página.

## Tabla de símbolos
Símbolo ID | Código entero
-- | :--:
Peso | -1
Identificadores | 0
Enteros | 1
Reales | 2
Cadenas | 3
Tipo | 4
Operador de suma | 5
Operador de resta | 6
Operador de multiplicación | 7
Operador de división | 8
Operador OR | 9
Operador AND | 10
Operador NOT | 11
Operador mayor que | 12
Operador menor que | 13
Operador mayor o igual que | 14
Operador menor o igual que | 15
Operador igual | 16
Operador es igual a | 17
Operador es diferente de | 18
Punto y coma | 19
Coma | 20
Parentesis abierto | 21
Parentesis cerrado | 22
Llave abierta | 23
Llave cerrada | 24
Bracket abierto | 25
Bracket cerrado | 26
Dos putos | 27
Palabra reservada: if | 50
Palabra reservada: while | 51
Palabra reservada: return | 52
Palabra reservada: else | 53
Palabra reservada: int | 54
Palabra reservada: float | 55
Palabra reservada: void | 56
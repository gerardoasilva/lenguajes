  
# -*- coding: utf-8 -*-

# Implementación de un scanner mediante la codificación de un Autómata
# Finito Determinista como una Matríz de Transiciones
# Autor: Dr. Santiago Conant, Agosto 2014 (modificado en Agosto 2015)

# INTEGRANTES
# Luis Alberto Caballero Noguez A01282700
# Gerardo Alfonso Silva 
# Jorge Elizondo

import sys

# tokens
INT = 100  # Número entero
LRP = 101  # Delimitador: paréntesis izquierdo
RRP = 102  # Delimitador: paréntesis derecho
BOO = 103  # Booleano
SMB = 104  # Simbolo
STR = 105  # String
END = 106  # Fin de la entrada
ERR = 200  # Error léxico: palabra desconocida

# Matriz de transiciones: codificación del AFD
# [renglón, columna] = [estado no final, transición]
# Estados > 99 son finales (ACEPTORES)
# Caso especial: Estado 200 = ERROR
#      dig   (    )   raro  esp  $    "    #     t    f   letr
MT = [[  1, LRP, RRP,   5,   0, END,   2,   4,   3,   3,   3], # edo 0 - estado inicial
      [  1, ERR, ERR, ERR, INT, INT, ERR, ERR, ERR, ERR, ERR], # edo 1 - dígitos enteros
      [  2, ERR, ERR, ERR,   2, ERR, STR, ERR,   2,   2,   2], # edo 2 - strings
      [ERR, ERR, ERR, ERR, SMB, ERR, ERR, ERR,   3,   3,   3], # edo 3 - simbolos
      [ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR, BOO, BOO, ERR], # edo 4 - booleanos
      [ERR, ERR, ERR,   5, ERR, ERR, ERR, ERR, ERR, ERR, ERR]] # edo 5 - estado de error
    
    

# Filtro de caracteres: regresa el número de columna de la matriz de transiciones
# de acuerdo al caracter dado
def filtro(c):
    """Regresa el número de columna asociado al tipo de caracter dado(c)"""
    if c == '0' or c == '1' or c == '2' or \
       c == '3' or c == '4' or c == '5' or \
       c == '6' or c == '7' or c == '8' or c == '9': # dígitos
        return 0
    elif c == '(': # delimitador (
        return 1
    elif c == ')': # delimitador )
        return 2
    elif c == ' ' or ord(c) == 9 or ord(c) == 10 or ord(c) == 13: # blancos
        return 4
    elif c == '$': # fin de entrada
        return 5
    elif c == '"': # String
        return 6
    elif c == '#': # Booleano
        return 7
    elif c == 't': # letra o booleano
        return 8
    elif c == 'f': # letra o booleano
        return 9
    elif (ord(c) >= 97 and ord(c) <= 122): # letras minusculas
        return 10
    else: # caracter raro
        return 3

_c = None    # siguiente caracter
_leer = True # indica si se requiere leer un caracter de la entrada estándar

# Función principal: implementa el análisis léxico
def obten_token():
    """Implementa un analizador léxico: lee los caracteres de la entrada estándar"""
    global _c, _leer
    edo = 0 # número de estado en el autómata
    lexema = "" # palabra que genera el token
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if _leer: _c = sys.stdin.read(1)
            else: _leer = True
            edo = MT[edo][filtro(_c)]
            if edo < 100 and edo != 0: lexema += _c
        if edo == INT:    
            _leer = False # ya se leyó el siguiente caracter
            print("Entero ", lexema)
            return INT
        elif edo == LRP:   
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador ", lexema)
            return LRP
        elif edo == RRP:  
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador ", lexema)
            return RRP          
        elif edo == STR:
            _leer = False
            print("String ", lexema)
            return STR
        elif edo == BOO:
            lexema += _c  # el último caracter forma el lexema
            print("Booleano ", lexema)
            return BOO
        elif edo == SMB:
            _leer = False
            print("Simbolo ", lexema)
            return BOO
        elif edo == END:
            print("Fin de expresion")
            return END
        else:   
            _leer = False # el último caracter no es raro
            print("ERROR! palabra ilegal", lexema)
            return ERR


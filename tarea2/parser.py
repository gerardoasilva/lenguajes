# INTEGRANTES
# A01136526 - Gerardo Silva
# A01282700 - Luis Caballero
# A01282508 - Jorge Elizondo

# Implementación de un parser
# Reconoce expresiones mediante la gramática:
# PROG      -> EXP PROG | $
# EXP       -> ATOMO | LISTA
# ATOMO     -> simbolo | CONSTANTE
# CONSTANTE -> numero | booleano | string
# LISTA     -> ( ELEMENTOS )
# ELEMENTOS -> EXP ELEMENTO | vacio
# los elementos léxicos (símbolos, números, booleanos, strings)
# son reconocidos por el scanner


import sys
# from obten_token import (
#     obten_token,
#     INT, 
#     LRP,
#     RRP,
#     BOO,
#     SMB,
#     STR,
#     END,
#     ERR
# )
import obten_token as scanner

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = scanner.obten_token()
    else:
        error("token equivocado")
        

# Función principal: implementa el análisis sintáctico
def parser():
    global token 
    token = scanner.obten_token() # inicializa con el primer token
    prog()
    if token == scanner.END:
        print("Expresion bien construida!!")
    else:
        error("expresion mal terminada")

def prog():
    exp()
    prog()

def exp():
    if (token == scanner.LRP):
        match(token) # delimitador (
        lista()
        match(scanner.RRP)   # delimitador )
    else:
        atomo()

def atomo():
    if (token == scanner.SMB):
        match(token) # Simbolo
    else:
        constante()

def constante():
    if (token == scanner.INT or token == scanner.BOO or token == scanner.STR):
        match(token) #constante

def lista():
        elementos()

def elementos():
        exp()
        elementos()

# Termina con un mensaje de error
def error(mensaje):
    print("ERROR:", mensaje)
    sys.exit(1)

parser()
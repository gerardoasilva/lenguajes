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
    #if token == scanner.END:
    #    print("Expresion bien construida!!")
    #else:
    #    error("Expresion mal terminada")

def prog():
    print("<prog>")
    if token == scanner.END:
        print(">>ENTRADA CORRECTA<<")
    else:
        exp()
        prog()


def exp():
    print("<exp>")  
    if token == scanner.INT or token == scanner.BOO or token == scanner.STR or  token == scanner.SMB:
        atomo()
    elif token == scanner.LRP:
        lista()
    else:
        error(">>ERROR SINTATICO<<")

def atomo():
    print("<atomo>")
    if token == scanner.SMB:
        match(token) # Simbolo
    else:
        constante()

def constante():
    if token == scanner.INT or token == scanner.BOO or token == scanner.STR:
        print("<constante>")
        match(token) #constante
    else:
        error(">>ERROR SINTATICO<<")

def lista():
    if (token == scanner.LRP):
        match(token) # delimitador (
        elementos()
        print("<lista>")
        match(scanner.RRP) # delimitador )
    else:
        error(">>ERROR SINTATICO<<")
    
def elementos():
    print("<elementos>")
    if token == scanner.INT or token == scanner.BOO or token == scanner.STR or token == scanner.SMB or token == scanner.LRP:
        exp()
        elementos()

# Termina con un mensaje de error
def error(mensaje):
    print(mensaje)
    sys.exit(1)

parser()


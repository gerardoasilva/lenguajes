# Implementación de un parser
# Reconoce expresiones mediante la gramática:
# EXP -> EXP op EXP | EXP -> (EXP) | cte
# la cual fué modificada para eliminar ambigüedad a:
# EXP  -> cte EXP1 | (EXP) EXP1
# EXP1 -> op EXP EXP1 | vacío
# los elementos léxicos (delimitadores, constantes y operadores)
# son reconocidos por el scanner

# ASIG  -> ide opa EXP
# EXP   -> ARIT | {COND}
# COND  -> EXP opr EXP ? EXP : EXP
# ARIT  -> cte ARIT1 | ide ARIT1 | (ARIT) ARIT1 | {COND}
# ARIT1 -> opb ARIT ARIT1 | e


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
        error("exp")

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


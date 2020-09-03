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
from obten_token import (
    obten_token,
    INT, 
    LRP,
    RRP,
    BOO,
    SMB,
    STR,
    END,
    ERR
)

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token

    # print('----')
    # print(f"token {token}")
    # print(f"token esperado {tokenEsperado}")
    # print('----')

    if token == tokenEsperado:
        token = obten_token()
    else:
        error("token equivocado")
        

# Función principal: implementa el análisis sintáctico
def parser():
    global token 
    token = obten_token() # inicializa con el primer token
    prog()
    if token == END:
        print("Expresion bien construida!!")
    else:
        error("expresion mal terminada")

def prog():
    exp()
    prog()

def exp():
    if (token == LRP):
        match(token) # delimitador (
        lista()
        match(RRP)   # delimitador )
    else:
        atomo()

def atomo():
    if (token == SMB):
        match(token) # Simbolo
    else:
        constante()

def constante():
    if (token == INT or token == BOO or token == STR):
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
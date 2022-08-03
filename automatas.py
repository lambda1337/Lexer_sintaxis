################ CONSTANTES #######################
LETRAS = list(map(chr, range(97, 123)))                                                #
LETRAS_MAYUS = list(map(lambda letter: letter.upper(),LETRAS))     #
NUMEROS = list(map(lambda number: str(number), range(0,10)))      #
################################################ #
ESTADO_FINAL = "ESTADO FINAL"                                                        #
ESTADO_NO_FINAL = "ESTADO NO FINAL"                                           #
ESTADO_TRAMPA = "ESTADO TRAMPA"                                                #
#################################################

############# AUTOMATA PARA CADA TOKEN VALIDO PROPUESTO EN LA GRAMATICA ##############
def a_id(cadena):
    estado_actual = 0
    for letra in cadena:
        if letra in (LETRAS or LETRAS_MAYUS) and estado_actual == 0:
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL

def a_num(cadena):
    estado_actual = 0
    for letra in cadena:
        if letra in NUMEROS and estado_actual == 0:
            estado_actual = 1
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL

def a_multiplicacion(cadena):
    estado_actual = 0
    for letra in cadena:
        if estado_actual == 0 and letra == "*":
            estado_actual = 1
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL

def a_parentesisAbierto(cadena):
    estado_actual = 0    
    for letra in cadena:
        if estado_actual == 0 and letra == "(":
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL

def a_parentesisCerrado(cadena):
    estado_actual = 0
    for letra in cadena:
        if estado_actual == 0 and letra == ")":
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL

def a_suma(cadena):
    estado_actual = 0
    for letra in cadena:
        if estado_actual == 0 and letra == "+":
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL

def a_si(cadena):
    estado_actual = 0
    estados_finales = [2]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 's':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'i':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def a_entonces(cadena):
    estado_actual = 0
    estados_finales = [8]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 'e':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'n':
            estado_actual = 2
        elif estado_actual == 2 and letra == 't':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'o':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'n':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'c':
            estado_actual = 6
        elif estado_actual == 6 and letra == 'e':
            estado_actual = 7
        elif estado_actual == 7 and letra == 's':
            estado_actual = 8
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def a_sino(cadena):
    estado_actual = 0
    estados_finales = [4]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 's':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'i':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'n':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'o':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def a_mostrar(cadena):
    estado_actual = 0
    estados_finales = [7]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 'm':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'o':
            estado_actual = 2
        elif estado_actual == 2 and letra == 's':
            estado_actual = 3
        elif estado_actual == 3 and letra == 't':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'r':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'a':
            estado_actual = 6
        elif estado_actual == 6 and letra == 'r':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def a_aceptar(cadena):
    estado_actual = 0
    estados_finales = [7]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 'a':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'c':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'e':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'p':
            estado_actual = 4
        elif estado_actual == 4 and letra == 't':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'a':
            estado_actual = 6
        elif estado_actual == 6 and letra == 'r':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def a_eq(cadena):
    estado_actual = 0
    estados_finales = [0]

    for letra in cadena:
        if letra == '=' and estado_actual == 0:
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL
import re as expresiones_regulares

# Algoritmo para ver si una cadena cumple
def test(cadena, test_cadena, automata):
    # asumo una supuesta cadena vacia
    supuesta_cadena = ""
    # por cada letra en la FILTRADA cadena 
    for letra in test_cadena:
        # a la supuesta cadena le sumo las letras de la filtrada
        supuesta_cadena += letra
    # luego, si el automata fue aceptado, la supuesta cadena, deberia ser igual a la cadena original
    # tambien retorno de que automata salio.
    return supuesta_cadena == cadena, automata

def AUTOMATA_IDS(cadena):
# regex de IDS
    test_cadena = expresiones_regulares.findall("\w",cadena)
    return test(cadena, test_cadena, "id")

def AUTOMATA_KEYWORDS(cadena):
# regex de palabras claves de los terminales
    test_cadena = expresiones_regulares.findall("esMenorQue|si|mientras|hacer|entonces|mostrar|aceptar|sino", cadena)
    return test(cadena, test_cadena, "keyword")

def AUTOMATA_NUMEROS(cadena):
# regex de solo NUMEROS
    test_cadena = expresiones_regulares.findall("\d", cadena)
    return test(cadena, test_cadena, "num")

def AUTOMATA_OPERADORES_MATEMATICOS(cadena):
# regex de operadores matematicos
    test_cadena = expresiones_regulares.findall("\+|\*", cadena)
    return test(cadena, test_cadena, "operador matematico")

def AUTOMATA_OPERADORES_RELACIONES(cadena):
# regex de relaciones matematicas
    test_cadena = expresiones_regulares.findall("<|>|=", cadena)
    return test(cadena, test_cadena, "relaciones")

def AUTOMATA_PARENTESIS(cadena):
# regex de parentesis
    test_cadena = expresiones_regulares.findall("\(|\)", cadena)
    return test(cadena, test_cadena, "parentesis")

TOKENS_POSIBLES = [("id", AUTOMATA_IDS), ("num", AUTOMATA_NUMEROS),
("operador matematico", AUTOMATA_OPERADORES_MATEMATICOS),
("relaciones", AUTOMATA_OPERADORES_RELACIONES), ("keywords", AUTOMATA_KEYWORDS),
 ("parentesis", AUTOMATA_PARENTESIS)]

def get_automata(string):
    ACEPTADOS = []
    for (tipo, automata) in TOKENS_POSIBLES:
        if automata(string)[0]:
            print(automata(string))
            ACEPTADOS.append(automata(string))
    return ACEPTADOS[-1]
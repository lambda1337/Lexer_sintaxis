from automatas import *

TOKENS_POSIBLES = [("eq", a_eq), ("num", a_num),
("+", a_suma) , ("*", a_multiplicacion),
("(", a_parentesisAbierto), (")", a_parentesisCerrado),
("si", a_si), ("entonces", a_entonces), ("sino", a_sino), 
("mostrar", a_mostrar), ("aceptar", a_aceptar), ("mientras", a_mientras),
("esMenorQue", a_esMenorQue), ("hacer", a_hacer), ("op", a_op),
("clp", a_clp), ("id", a_id)]

def get_automata(lexema):
    for (token, automata) in TOKENS_POSIBLES:
        if automata(lexema) == ESTADO_FINAL:
            yield (automata.__name__)

def lexer(source_code):
    # añado espacio al final ya que si no, no reconoce el ultimo caracter debido al algoritmo implementado
    source_code += " "
    # caracteres acumulados hasta ahora
    lexema = ""
    #tokens_validos
    tokens_validos = []
    tokens_invalidos = []
    # inicio de palabra o expresion
    from_zero = 0
    # fin de expresion
    to_end = 0
    # por cada expresion en el codigo fuente
    for expresion in source_code:
        # añado +1 al to_end del fin expresion
        to_end += 1
        # si NO es un espacio, le añado el caracter a acumulated
        if expresion != " ":
            lexema += expresion
        # si es un espacio, significa que llegue al fin de expresion
        else:
            # añado a tokens_validos lo que salga del automata, aunque primero deberia revisar si alguno devuelve algo...
            automatas_posibles = []

            # me fijo los automatas que llegan a estado final con este lexema
            for automata in get_automata(lexema):
                automatas_posibles.append(automata)

            # si no hay automatas posibles significa que todos cayeron en trampa, osea es invalido
            if len(automatas_posibles) == 0:
                # agrego el token invalido
                tokens_invalidos.append(lexema)
            else:
                # agrego el token valido
                tokens_validos.append((automatas_posibles[0], ''.join(source_code[from_zero:to_end-1])))
            # reseteo el lexema, ya que finalizo una expresion
            lexema = ""
            # al from_zero lo igualo a to_end , ya que avanzamos en el codigo fuente
            from_zero = to_end
    # retorno los tokens validos e invalidos
    return tokens_validos, tokens_invalidos

resultado = lexer("si 5 %%·$·% esMenorQue $$ 4 hacer mostrar 10 entonces aceptar 15")
print( "\n\n - Invalidos: ",resultado[1], "\n Validos: ", resultado[0])

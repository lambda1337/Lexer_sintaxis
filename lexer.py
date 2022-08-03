from listado_automatas import *

def lexer(source_code):
    # añado espacio al final ya que si no, no reconoce el ultimo caracter debido al algoritmo implementado
    source_code += " "
    # caracteres acumulados hasta ahora
    acumulated = ""
    #tokens_validos
    tokens_validos = []
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
            acumulated += expresion
        # si es un espacio, significa que llegue al fin de expresion
        else:
            # añado a tokens_validos lo que salga del automata, aunque primero deberia revisar si alguno devuelve algo...
            tokens_validos.append((get_automata(acumulated)[1], ''.join(source_code[from_zero:to_end-1])))
            # reseteo el acumulated, ya que finalizo una expresion
            acumulated = ""
            # al from_zero lo igualo a to_end , ya que avanzamos en el codigo fuente
            from_zero = to_end
    # retorno los tokens validos
    return tokens_validos

print(lexer("si 5 > 4 hacer mostrar 10 entonces aceptar 15"))

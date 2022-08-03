from listado_automatas import *

def lexer(source_code):
    source_code += " "
    source_code = expresiones_regulares.findall(".", source_code)
    acumulated = ""
    tokens_validos = []
    from_zero = 0
    to_end = 0
    for expresion in source_code:
        to_end += 1
        if expresion != " ":
            acumulated += expresion
        else:
            tokens_validos.append((get_automata(acumulated)[1], ''.join(source_code[from_zero:to_end-1])))
            acumulated = ""
            from_zero = to_end

    return tokens_validos

print(lexer("si 5 > 4 hacer mostrar 10 entonces aceptar 15"))
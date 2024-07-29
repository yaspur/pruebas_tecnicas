"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 64:
Crea un programa que compruebe si los paréntesis, llaves y corchetes 
de una expresión están equilibrados, es decir, que estos delimitadores 
se abren y cieran de forma adecuada.
 
Ejemplos:
expresionEquilibrada('{ [ x * ( y + z ) ] * 12 }');  // imprime true
expresionEquilibrada('{ x * ( y + z ) ] + 12 }');  // imprime false
"""

def expresionEquilibrada(expresion):

    # Inicializar contadores para parentesis, llaves y corchetes
    parentesis_abiertos = expresion.count("(")
    parentesis_cerrados = expresion.count(")")

    llaves_abiertos = expresion.count("[")
    llaves_cerrados = expresion.count("]")

    corchetes_abiertos = expresion.count("{")
    corchetes_cerrados = expresion.count("}")

    if ((parentesis_abiertos == parentesis_cerrados) and (llaves_abiertos == llaves_cerrados) and (corchetes_abiertos == corchetes_cerrados)):
        return True
    else:
        return False
    
print(expresionEquilibrada('{ [ x * ( y + z ) ] * 12 }'))
print(expresionEquilibrada('{ x * ( y + z ) ] + 12 }'))
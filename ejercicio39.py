"""
/*
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 39:
Dado un número crea una función que genere todas las combinaciones
de parentesis válidas.
 
Ejemplos:
combinacionesParentesis(3);
 
Devuelve:
[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
*/
"""

contador_ejecuciones = 0

def generar_parentesis(combinacion, abiertos, cerrados, resultados):

    if abiertos == 0 and cerrados == 0:
        resultados.append(combinacion)
        return
    
    if abiertos > 0:
        generar_parentesis(combinacion + "(", abiertos - 1, cerrados, resultados)
        
    if cerrados > 0 and abiertos < cerrados:
        generar_parentesis(combinacion + ")", abiertos, cerrados - 1, resultados)
        

def combinaciones_parentesis(numero_combinacion):
    
    resultados = []
    
    if numero_combinacion < 1:
        return resultados
    
    generar_parentesis('', numero_combinacion, numero_combinacion, resultados)
    
    return resultados

print(combinaciones_parentesis(3))
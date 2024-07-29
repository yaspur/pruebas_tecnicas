"""
/*
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 40:
Crea una función que convierta un número romano a decimal.
 
Ejemplos:
romanoAEntero("XVIII")   // 18
romanoAEntero("CXX")     // 120
 
*/
"""

def romano_a_entero(numero_romano):
    
    tabla_romanos = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    
    resultado = 0
    
    for i in range(len(numero_romano)):
        
        if i == len(numero_romano) - 1 or tabla_romanos[numero_romano[i + 1]] <= tabla_romanos[numero_romano[i]]:
            resultado += tabla_romanos[numero_romano[i]]
            
        else:
            resultado -= tabla_romanos[numero_romano[i]]

    return resultado

print(romano_a_entero("XIV"))
print(romano_a_entero("CXX"))

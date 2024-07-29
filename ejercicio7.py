"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 7:
Dada un array de enteros, detectar si esa lista
de números es una permutación del 1 al ultimo número del array.
 
En este caso una permutación es una secuencia de números
en orden sin que falte ninguno entre ellos.
 
Devolver el número faltante más grande.
 
El array puede venir desordenado.
 
Ejemplos:
permutacion([1, 2, 3, 4, 5])   // Devuelve: 5
permutacion([1, 2, 3, 5]))     // Devuelve: 4
"""

def permutacion(numeros: list):

    numeros.sort()
    rango_numeros = numeros[-1]
    numeros_faltantes = []

    for i in range(rango_numeros):
        
        numero_falta = i + 1
        if numero_falta not in numeros:
            numeros_faltantes.append(numero_falta)

    if numeros_faltantes:
        return numeros_faltantes[-1]
    else: 
        return numeros[-1]


print(permutacion([1, 2, 3, 4, 5, 6]))
print(permutacion([1, 2, 4, 6, 10]))




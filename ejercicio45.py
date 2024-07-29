"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 45:
Dado un array de números, elimina los números duplicados.
 
Ejemplos:
eliminarDuplicados([1, 1, 2, 2, 3, 4, 5, 5, 5, 6])
 
Devuelve:
[ 1, 2, 3, 4, 5, 6 ]
"""

#def eliminarDuplicados(arr):
#    return list(set(arr))

def eliminarDuplicados(arr):
     
    sin_duplicados = []

    for elemento in arr:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    
    return sin_duplicados



print(eliminarDuplicados([1, 1, 2, 2, 3, 4, 5, 5, 5, 6]))



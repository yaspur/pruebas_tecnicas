"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 30:
Dado un array de numeros, permitir los numeros duplicados
un maximo de 2 veces y devolver la longitud del array.
 
Ejemplos:
eliminarDuplicados([4, 4, 4, 2, 2, 3]); // 5
eliminarDuplicados([6, 6, 2, 2, 2, 3]); // 5
eliminarDuplicados([1, 2, 3, 4, 9, 9, 9, 9]); // 5
"""

def eliminarDuplicados(numeros):

    cantidad_numeros = {}
    lista_numeros = []

    for numero in numeros:

        if str(numero) in cantidad_numeros:
            cantidad_numeros[str(numero)] += 1
        else:
            cantidad_numeros[str(numero)] = 1

        if cantidad_numeros[str(numero)] <= 2:
            lista_numeros.append(numero)

    print(lista_numeros)

    return len(lista_numeros)

print(eliminarDuplicados([4, 4, 4, 2, 2, 3])); # 5
print(eliminarDuplicados([6, 6, 2, 2, 2, 3])) # 5
print(eliminarDuplicados([1, 2, 3, 4, 9, 9, 9, 9])) #5
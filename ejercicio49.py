"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 49:
Crea una función que dado un array de números devuelva el número 
más pequeño de la matriz.
 
No puedes ordenar el array, solo usar estructuras de control.
 
Ejemplos:
elMasPequenio([8,9,99,88,77,1,12,13,6,7])  // Devuelve: 1
"""

def elMasPequenio(arrNum):

    numero_menor = arrNum[0]

    for numero in arrNum:
        if numero <= numero_menor:
            numero_menor = numero

    return numero_menor


print(elMasPequenio([8,9,99,88,77,5,12,13,3,7]))






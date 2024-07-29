"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 63:
Crea una función para conseguir las sumas acumuladas de una array de numeros
 
Ejemplos:
sumasAcumuladas([1, 2, 3, 4])   // [1, 3, 6, 10] 
 
(se calcula como: [1, 1+2, 1+2+3, 1+2+3+4])
"""

def sumasAcumuladas(arrNum):

    # Inicializa una lista vacia donde guardarás las sumas acumuladas
    accList = []
    
    # Recorre el array de números desde el primer elemento hasta el último
    for i in range(len(arrNum)):

        if i == 0:
            accList.insert(i, arrNum[i])
        else:
            accList.insert(i, accList[i - 1] + arrNum[i])

    return accList

print(sumasAcumuladas([1,2,3,4]))








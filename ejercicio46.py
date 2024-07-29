"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 46:
Crea una función a la que le pasemos una nota y nos de una calificación:
 
0-3: Deficiente
3-5: Insuficiente
5-6: Suficiente
6-7: Bien
7-9: Notable
9-10: Sobresaliente
 
Ejemplos:
calificar(8.2) // Notable
"""

def calificar(nota):

    if nota >= 0 and nota <= 2.9:
        print("Deficiente")
    elif nota >= 3 and nota <= 4.9:
        print("Insuficiente")
    elif nota >= 5 and nota <= 5.9:
        print("Suficiente")
    elif nota >= 6 and nota <= 6.9:
        print("Bien")
    elif nota >= 7 and nota <= 8.9:
        print("Notable")
    elif nota >= 9 and nota <= 10:
        print("Sobresaliente")
    else:
        print("No es una nota valida")

calificar(1)    


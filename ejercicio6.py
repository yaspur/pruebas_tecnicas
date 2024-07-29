"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 6:
Dado un año actual, crea un programa que me muestre 
los años bisiestos que habrá en los proximos 30 años
 
Ejemplo:
bisiestos(2023);
 
Salida:
2024
2028
2032
2036
2040
2044
2048
2052
"""

import calendar

def existe_dia(year, month, day):
    return day <= calendar.monthrange(year, month)[1]

def bisiestos(year):

    limite = 30

    for _ in range(limite):

        if existe_dia(year, 2, 29):
            print(year)

        year += 1


print(bisiestos(2023))


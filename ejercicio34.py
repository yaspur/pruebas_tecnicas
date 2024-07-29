"""
/*
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 34:
Crea una función a la cual le pase un array y me devuelva 
un objeto con los elementos agrupados
 
Ejemplos:
agrupar([7.2, 5.3, 7.4], Math.floor)  
Devuelve: { 7: [7.2, 7.4], 5: [5.3] }
 
agrupar(['uno', 'dos', 'tres', 'cuatro'], 'length') 
Devuelve: { 3: ['uno', 'dos', 'tres'], 6: ['cuatro'] }
 
agrupar([{nombre: "victor", edad: 33}, {nombre: "paco", edad: 44}], 'edad') 
Devuelve: { 33: [{edad: 33}], 44: [{edad: 44}] }
 
*/
"""

import math

def agrupar(elementos: list, clave_agrupacion):
    resultado = {}
    
    for elemento in elementos:
        
        propiedad = clave_agrupacion(elemento) if callable(clave_agrupacion) else elemento[clave_agrupacion]
        
        if propiedad not in resultado:
            resultado[propiedad] = []
            
        resultado[propiedad].append(elemento)
        
    return resultado

# agrupar([7.2, 5.3, 7.4], math.floor)
# agrupar(['uno', 'dos', 'tres', 'cuatro'], len) 
print(agrupar([{"nombre": "victor", "edad": 33}, {"nombre": "paco", "edad": 44}], 'edad') )
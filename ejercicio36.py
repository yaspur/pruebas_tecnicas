"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 36:
Crea un programa que encuentre las parejas de números que como resultado
dan un número que pasamos a la función por parametro.
 
Ejemplos:
encontrarParejasConSuma([1, 2, 3, 4], 5);
 
Devuelve: 
[ [ 1, 4 ], [ 2, 3 ] ]
"""

def encontrar_parejas_suma(numeros_list, resultado):
    
    resultados = []
    
    for index, numero in enumerate(numeros_list):
        
        parejas = numeros_list[index:]
        
        for pareja in parejas:
            
            if numero + pareja == resultado:
                
                resultados.append([numero, pareja])
                
    return resultados

print(encontrar_parejas_suma([1,2,3,4], 5))  
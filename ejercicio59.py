"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 59:
Crea una función que retorne el número total de bumeranes de un 
array de números enteros e imprima cada uno de ellos.
 
Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números seguidos, 
en el que el primero y el último son iguales, y el segundo es diferente. 
Por ejemplo [2, 1, 2].
 
Ejemplos:
contrarBumeranes([2, 1, 2, 3, 3, 4, 2, 4])
 
Devuelve:
Hay 2 bumeranes: [[2, 1, 2], [4, 2, 4]]
"""

def contarBumeranes(lista):
    
    total_bumeranes = []
    
    for i in range(len(lista)):
        
        bumerang = lista[i:i+3]
        
        if len(bumerang) != 3:
            break
        
        if (bumerang[0] == bumerang[-1]) and (bumerang[1] != bumerang[0]):
            
            total_bumeranes.append(bumerang)
            
    return f"Hay {len(total_bumeranes)} bumeranes: {total_bumeranes}"

print(contarBumeranes([2, 1, 2, 3, 3, 4, 2, 4]))
        
        
        

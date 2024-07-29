"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 38:
Crea una función que convierta un número a binario.
 
Ejemplos:
aBinario(10) // 1010
aBinario(76) // 1001100
"""

def aBinario(decimal):
    
    binario = []
    
    while True:
        
        if decimal % 2 == 0:
            
            binario.append(0)
        
        else: 
            
            binario.append(1)
            
        decimal = decimal // 2
        
        if decimal == 1:
            binario.append(1)
            break
        
    binario.reverse()
    
    return "".join(map(str,binario))
    
print(aBinario(76))
    
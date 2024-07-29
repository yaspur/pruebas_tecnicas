"""
/*
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 51:
Crea una función que dibuje un diamante de asteriscos.
 
Ejemplos:
generarDiamante(5);
 
Devuelve: 
  *
 *** 
*****
 *** 
  *  
 
*/
 
"""

import math

def generar_diamante(numero):
    
    if numero % 2 == 0:
       return
   
    mitad = math.floor(numero/2)
    
    for fila_actual in range(numero):
        
        fila = ""
        
        espacios =  abs(mitad - fila_actual)
        
        
        espacio_actual = 0
        while espacio_actual < espacios:
            
            fila += " "
            espacio_actual += 1
            
        asterisco_actual = 0
        while asterisco_actual < numero - (espacios * 2):
            
            fila += "*"
            asterisco_actual += 1
            
        print(fila) 
            
generar_diamante(5)
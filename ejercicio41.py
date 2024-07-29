"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 41:
Crea una función que invierta los números de un número entero.
 
Ejemplos:
invertirEntero(123)   // 321
invertirEntero(-123)  // -321
"""

def invertirEntero(numero):

    numero = str(numero)
    numero_invertido = ""

    for i in range(len(numero) - 1, -1, -1):
        if numero[i] == "-":
            numero_invertido = "-" + numero_invertido
        else:
            numero_invertido += numero[i]
    
    return int(numero_invertido)

print(invertirEntero(123))   # 321
print(invertirEntero(-123))  #-321


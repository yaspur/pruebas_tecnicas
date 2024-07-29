"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 68:
Crea una función que pueda generar contraseñas aleatorias.
 
Podrás pasar los siguientnes parámetros para las contraseñas:
- Longitud: Entre 6 y 20.
- Con o sin mayúsculas.
- Con o sin números.
- Con o sin símbolos.
 
Ejemplos:
generarContrasenia(12, true, true, false);
"""

import random
import string


def generarContrasenia(longitud, tiene_mayus, tiene_numeros, tiene_simbolos):

    if longitud < 1 and longitud > 20:
        return "Longitud invalida"
    
    caracteres = string.ascii_lowercase
    if tiene_mayus:
        caracteres += string.ascii_uppercase
    if tiene_numeros:
        caracteres += string.digits
    if tiene_simbolos:
        caracteres += string.punctuation

    contrasenia = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasenia

print(generarContrasenia(12, True, True, False))
    





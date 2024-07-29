"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 31:
Dado un texto, crea una función que sea capaz de invertir
el orden de sus palabras.
 
No podemos usar funciones nativas del lenguaje.
 
Ejemplos:
invertirPalabras("Hola soy Victor Robles"); // Devuelve: Robles Victor soy Hola
"""

def invertirPalabras(palabra):

    palabra = palabra.split()
    palabra_invertida = ""

    for i in range(len(palabra) - 1, -1, -1):
        
        if len(palabra[i]) >= 1:
            palabra_invertida += palabra[i] + " "

    return palabra_invertida.rstrip()


print(invertirPalabras('Hola Yasid Pumarejo'))
print(invertirPalabras('Hola soy Victor Robles'))
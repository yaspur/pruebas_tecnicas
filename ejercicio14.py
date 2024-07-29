"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 14:
Dada una cadena de texto, comprobar si es un palindromo o no. No usar funciones de
javascript, solo estructuras de control
 
Los palíndromos son palabras que se leen igual aun estando invertidas. 
Por ejemplo: ana, bob, otto, allivessevilla
 
Ejemplos:
esPalindromo("otto") // Devuelve: true
esPalindromo("victor") // Devuelve: false
"""

def esPalindromo(texto):
    cadena = texto.replace(' ', '')
    return cadena == cadena[::-1]

def esPalindromo_dos(texto):

    cadena = texto.replace(' ', '')

    letras_inversa = []

    for i in range(len(cadena)-1,-1,-1):

        letras_inversa.append(cadena[i])

    letras_inversa = "".join(letras_inversa)

    return letras_inversa == cadena



print(esPalindromo("otto"))
print(esPalindromo_dos("otto"))
print(esPalindromo("victor"))
print(esPalindromo_dos("victor"))





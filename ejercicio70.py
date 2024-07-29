"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 70:
Crea una función que dado un texto que contenga varias frases en minusculas,
logre poner en mayusculas las letras correctas del texto. 
 
Ejemplos:
capitalizarFrase("hola. como estas. soy Víctor Robles. me gusta programar.");
 
Devuelve:
Hola. Como estas. Soy Victor Robles. Me gusta programar.
"""

def capitalizarFrase(frase: str):
    # Separamos la frase en palabras
    palabras = frase.split(".")

    frases_capitalizadas = []

    for palabra in palabras:

        if palabra != "":

            letra = palabra.strip()[0].upper()
            restante = palabra.strip()[1:]
            frases_capitalizadas.append(letra + restante)

    return ". ".join(frases_capitalizadas) + "."
    
print(capitalizarFrase("hola. como estas. soy Víctor Robles. me gusta programar."))
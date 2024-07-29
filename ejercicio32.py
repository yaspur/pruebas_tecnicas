"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 32:
Dado un texto, crea una función que sea capaz de generar
un nuevo texto que incluya solo las palabras de 4 caracteres o más.
 
Ejemplos:
fraseFiltrada("Hola soy Victor Robles, hoy hace frio"); 
 
Devuelve: Hola Victor Robles, hace frio
"""

def fraseFiltrada(texto):
    # Crea una lista con todas las palabras del texto separadas en elementos individuales
    palabras = texto.split()
    
    # Recorre cada elemento de la lista y comprueba si tiene 4 o mas caracteres
    filtroPalabras = [palabra for palabra in palabras if len(palabra) >= 4]
    
    # Devuelve la nueva frase formada por las palabras filtradas
    return ' '.join(filtroPalabras)

# Pruebas
print(fraseFiltrada("Hola soy Victor Robles, hoy hace frio"))   # "Hola Victor Robles, hace frio"
print(fraseFiltrada("Python es un lenguaje muy interesante"))
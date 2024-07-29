"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 5:
Dado un array de personas con nombres y apellidos
crear una función para ordenar el array por los apellidos
en orden alfabético
 
Ejemplo:
ordenarPorApellidos([
    "Víctor Robles",
    "Antonio Alcantara",
    "Al Pacino",
    "Robert DeNiro",
    "Brad Pitt",
    "Sylvester Stallone"
]);  
"""

letras = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "ñ": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

def ordenarPorApellido(nombres: list):

    apellidos_ordenados = []

    while nombres:

        primer_letra_apellido_inicial = nombres[0].split(" ")[1][0].lower()
        valor_letra_inicial = letras[primer_letra_apellido_inicial]
        agregar_palabra = ""

        for nombre in nombres:
            
            primer_letra_apellido = nombre.split(" ")[1][0].lower()
            valor_letra_apellido = letras[primer_letra_apellido]

            if valor_letra_apellido <= valor_letra_inicial:
                agregar_palabra = nombre
                valor_letra_inicial = valor_letra_apellido

        apellidos_ordenados.append(agregar_palabra)
        nombres.remove(agregar_palabra)
    
    return apellidos_ordenados

nombres = [
    "Víctor Robles",
    "Antonio Alcantara",
    "Al Pacino",
    "Robert DeNiro",
    "Brad Pitt",
    "Sylvester Stallone"
]

def ordenarPorApellido_2(personas):

    apellidos = [nombre.split(" ")[1] for nombre in personas]

    apellidos.sort()

    nombres_ordenados = []

    for apellido in apellidos:

        for nombre in personas:

            if apellido in nombre:

                nombres_ordenados.append(nombre)

    return nombres_ordenados

print(ordenarPorApellido_2([
    "Víctor Robles",
    "Antonio Alcantara",
    "Al Pacino",
    "Robert DeNiro",
    "Brad Pitt",
    "Sylvester Stallone"
]))
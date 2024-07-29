"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 29:
Dado un array de objetos de peliculas de los años 80 y 90. 
 
Crea dos funciones:
- Una que las filtre por género
- y otra que las filtre por la decada en este formato 80s o 90s
 
Array de objetos a utilizar:
const peliculas = [
    { titulo: "Terminator", genero: "accion", anioLanzamiento: 1984 },
    { titulo: "Alien", genero: "ciencia ficción", anioLanzamiento: 1979 },
    { titulo: "Die Hard", genero: "accion", anioLanzamiento: 1988 },
    { titulo: "Predator", genero: "accion", anioLanzamiento: 1987 },
    { titulo: "Total Recall", genero: "ciencia ficción", anioLanzamiento: 1990 },
    { titulo: "RoboCop", genero: "ciencia ficción", anioLanzamiento: 1987 },
    { titulo: "Starship Troopers", genero: "ciencia ficción", anioLanzamiento: 1997 },
    { titulo: "The Fifth Element", genero: "ciencia ficción", anioLanzamiento: 1997 },
    { titulo: "Armageddon", genero: "accion", anioLanzamiento: 1998 },
    { titulo: "Deep Impact", genero: "ciencia ficción", anioLanzamiento: 1998 }
  ];
 
Ejemplos:
filtrarPorGenero(peliculas, "accion")
filtrarPorDecada(peliculas, "80s")
"""

def filtradoPorGenero(peliculas, genero):

    lista_filtrada = []

    for pelicula in peliculas:

        if genero == pelicula["genero"]:
            lista_filtrada.append(pelicula)
    
    return lista_filtrada

def filtradoPorGenero_dos(peliculas, genero):

    peliculas_por_genero = filter(lambda pelicula: pelicula["genero"] == genero, peliculas)

    # Convertir el iterador a una lista para ver los resultados
    peliculas_por_genero = list(peliculas_por_genero)
    
    return peliculas_por_genero

def filtradoPorDecada(peliculas, decada):

    lista_filtrada = []
    anio_inicio = 0
    anio_final = 0

    if decada == "80s":

        anio_inicio = 1980
        anio_final = 1989

    elif decada == "90s":

        anio_inicio = 1990
        anio_final = 1999

    for pelicula in peliculas:

        if  anio_inicio <= pelicula["anioLanzamiento"] <= anio_final :
            
            lista_filtrada.append(pelicula)

    return f"Filtradas por década {decada}: \n{lista_filtrada}"

peliculas = [
    {"titulo": "Terminator", "genero": "accion", "anioLanzamiento": 1984},
    {"titulo": "Alien", "genero": "ciencia ficción", "anioLanzamiento": 1979},
    {"titulo": "Die Hard", "genero": "accion", "anioLanzamiento": 1988},
    {"titulo": "Predator", "genero": "accion", "anioLanzamiento": 1987},
    {"titulo": "Total Recall", "genero": "ciencia ficción", "anioLanzamiento": 1990},
    {"titulo": "RoboCop", "genero": "ciencia ficción", "anioLanzamiento": 1987},
    {"titulo": "Starship Troopers", "genero": "ciencia ficción", "anioLanzamiento": 1997},
    {"titulo": "The Fifth Element", "genero": "ciencia ficción", "anioLanzamiento": 1997},
    {"titulo": "Armageddon", "genero": "accion", "anioLanzamiento": 1998},
    {"titulo": "Deep Impact", "genero": "ciencia ficción", "anioLanzamiento": 1998}
]

print(filtradoPorGenero_dos(peliculas, "accion"))
#print(filtradoPorDecada(peliculas, "90s"))









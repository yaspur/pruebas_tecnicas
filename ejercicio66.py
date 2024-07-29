"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 66:
Crea una función que pueda filtrar la información de los superhéroes por afiliación. 
Puedes hacer que la función tome una afiliación como parámetro 
y muestre la información de los superhéroes que pertenecen a esa afiliación.
 
Ejemplos:
filtrarPorAfiliacion(personajesDC, 'Crimen organizado')
"""

personajesDC = {
    "Superman": {
        "nombreReal": "Clark Kent",
        "poderes": ["SuperFuerza", "Vuelo", "Vision laser"],
        "afiliacion": "Justice League"
    },
    "Batman": {
        "nombreReal": "Bruce Wayne",
        "poderes": ["Inteligencia", "Dinero"],
        "afiliacion": "Justice League"
    },
    "Joker": {
        "nombreReal": "Unknow",
        "poderes": ["Manipulacion", "Inteligencia"],
        "afiliacion": "Crimen Organizado"
    },
    "Harley Queen":{
        "nombreReal": "Harleen Quinzel",
        "poderes": ["Manipulacion", "Artes marciales"],
        "afiliacion": "Crimen Organizado"
    },
}

def filtrarPorAfiliacion(personajes, afiliacion):

    filtro_afiliacion = {}

    for personaje in personajes.keys():

        if personajes[personaje]["afiliacion"] == afiliacion:
            filtro_afiliacion[personaje] = personajes[personaje]

    return filtro_afiliacion

print(filtrarPorAfiliacion(personajesDC, "Crimen Organizado"))

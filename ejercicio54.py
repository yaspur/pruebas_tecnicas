"""
/*
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 54:
En la película de Avatar, existen diferentes tribus de Na'vi 
que habitan Pandora. Cada tribu tiene una habilidad especial y 
un valor de poder entre 1 y 5:
 
Tribus pacifistas: Omaticaya (1), Tawkami (2), Kekunan (3)
Tribus guerreras: Rda (2), Hometree (3), Toruk Makto (5)
 
Crea un programa que calcule el resultado de una guerra 
entre dos ejércitos de Na'vi. 
 
Ejemplos:
calcularResultadoGuerra(tribusBuenas, tribusMalas);
 
Devuelve:
"¡Gana el mal!"
*/
 
const tribusBuenas = [
    { nombre: { valor: 1, nombre: "Omaticaya" }, cantidad: 10 }, 10
    { nombre: { valor: 2, nombre: "Tawkami" }, cantidad: 5 }, 10
    { nombre: { valor: 3, nombre: "Kekunan" }, cantidad: 13 }, 29
];                                                              49
 
const tribusMalas = [
    { nombre: { valor: 2, nombre: "Rda" }, cantidad: 10 }, 20
    { nombre: { valor: 3, nombre: "Hometree" }, cantidad: 5 }, 15
    { nombre: { valor: 5, nombre: "Toruk Makto" }, cantidad: 1 }, 5
];
"""

def  calcularResultadoGuerra(tribusBuenas, tribusMalas):
    
    poder_tribus_buenas = 0
    poder_tribus_malas = 0

    #Tribus buenas
    for tribu_buena in tribusBuenas:

        cantidad_guerreros = tribu_buena["cantidad"]
        valor_guerrero = tribu_buena["nombre"]["valor"]

        poder_tribus_buenas += cantidad_guerreros * valor_guerrero

    #Tribus buenas
    for tribu_mala in tribusMalas:

        cantidad_guerreros = tribu_mala["cantidad"]

        for _ in range(cantidad_guerreros):

            poder_tribus_malas += tribu_mala["nombre"]["valor"]

    
    if poder_tribus_buenas > poder_tribus_malas:
        return "Gano el bien!"
    elif poder_tribus_buenas < poder_tribus_malas:
        return "Gano el mal!"
    else:
        return "Empate entre tribus"

tribusBuenas = [
    { "nombre": { "valor": 1, "nombre": "Omaticaya" }, "cantidad": 10 },
    { "nombre": { "valor": 2, "nombre": "Tawkami" }, "cantidad": 5 },
    { "nombre": { "valor": 3, "nombre": "Kekunan" }, "cantidad": 13 },
];
 
tribusMalas = [
    { "nombre": { "valor": 2, "nombre": "Rda" }, "cantidad": 10 },
    { "nombre": { "valor": 3, "nombre": "Hometree" }, "cantidad": 5 },
    { "nombre": { "valor": 5, "nombre": "Toruk Makto" }, "cantidad": 1 },
]


print(calcularResultadoGuerra(tribusBuenas, tribusMalas))
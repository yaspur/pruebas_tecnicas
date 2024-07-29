"""
/*
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 47:
Crea un simulador de pieda, papel o tijera.
 
El resultado podrá ser: "Jugador 1", Jugador 2" o "Empate"
 
Ejemplos:
 
quienGana([["PIEDRA", "TIJERA"], ["TIJERA", "PIEDRA"], ["PAPEL", "TIJERA"]]); 
Devuelve: "Jugador 2"
 
quienGana([["PIEDRA", "PIEDRA"], ["TIJERA", "TIJERA"], ["PAPEL", "PAPEL"]]); 
Devuelve: "Empate"
 
quienGana([["PIEDRA", "TIJERA"], ["TIJERA", "PAPEL"], ["PAPEL", "PIEDRA"]]); 
Devuelve "Jugador 1"
*/
"""

def quienGana(jugadas):

    puntos = {
        "jugador_1": 0,
        "jugador_2": 0
    }
    
    for i in range(len(jugadas)):
        
        jugada_jugador1 = jugadas[i][0]
        jugada_jugador2 = jugadas[i][1]

        if ((jugada_jugador1 == 'PIEDRA' and jugada_jugador2 == 'TIJERA') or 
            (jugada_jugador1 == 'TIJERA' and jugada_jugador2 == 'PAPEL') or  
            (jugada_jugador1 == 'PAPEL' and jugada_jugador2 == 'PIEDRA')):

            puntos['jugador_1'] += 1

        if ((jugada_jugador2 == 'PIEDRA' and jugada_jugador1 == 'TIJERA') or 
            (jugada_jugador2 == 'TIJERA' and jugada_jugador1 == 'PAPEL') or  
            (jugada_jugador2 == 'PAPEL' and jugada_jugador1 == 'PIEDRA')):

            puntos['jugador_2'] += 1

    if puntos['jugador_1'] > puntos['jugador_2']:
        return "Jugador 1"
    elif puntos['jugador_2'] > puntos['jugador_1']:
        return "Jugador 2"
    else:
        return "Empate"


print(quienGana([["PIEDRA", "TIJERA"], ["TIJERA", "PIEDRA"], ["PAPEL", "TIJERA"]]))
print(quienGana([["PIEDRA", "PIEDRA"], ["TIJERA", "TIJERA"], ["PAPEL", "PAPEL"]]))
print(quienGana([["PIEDRA", "TIJERA"], ["TIJERA", "PAPEL"], ["PAPEL", "PIEDRA"]]))




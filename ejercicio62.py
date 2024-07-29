"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 62:
Dado un diccionario de letras disponibles:
[
   ['A','B','C','D'],
   ['S','V','C','S'],
   ['A','D','O','E']
 ]
 
 Crea una función que me diga si la palabra que le paso
 como parametro se puede formar con las letras del
 diccionario disponibles.
 
¡PERO OJO! Cada vez que se usa una letra, se eliminia del array.
 
Ejemplos:
puedeFormarPalabra('BESO', diccionario)   // true
puedeFormarPalabra('SOSO', diccionario)   // false   
"""

def puedeFormarPalabra(palabra: str, coleccion: list):

    for letra in palabra:

        resultados_validacion = []

        for fila in coleccion:
            resultados_validacion.append(letra in fila)
            if letra in fila:
                fila.remove(letra)

        if True in resultados_validacion:
            continue
        else:
            return False
        
    return True

diccionario = [
   ['A','B','C','D'],
   ['S','V','C','S'],
   ['A','D','O','E']
 ]

print(puedeFormarPalabra('BESO', diccionario))
print(puedeFormarPalabra('SOSO', diccionario))
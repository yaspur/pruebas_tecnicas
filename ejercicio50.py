"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 50:
Crea una función que dada una temperatura la pase a grados
celsius o grados fahrenheit.
 
Ejemplos:
convertirTemperatura('29°C')  // Devuelve: "84.20°F"
convertirTemperatura('77°F')  // Devuelve: "25.00°C"
"""

def convertirTemperatura(temp):

    if 'C' in temp: # Si hay una C es Celsius
        celsius = float(temp[:-2])
        fahrenheit = (celsius * 9/5) + 32
        return f'{fahrenheit}°F'
    elif 'F' in temp: # Si hay una F es Fahrenheit
        fahrenheit = float(temp[:-2])
        celsius = (fahrenheit - 32) * 5/9
        return f'{celsius}°C'
    else:
        return "La temperatura debe ser en Celsius o Fahrenheit"

# Pruebas
print(convertirTemperatura('29°C'))   # "84.
print(convertirTemperatura('77°F'))   # "84.




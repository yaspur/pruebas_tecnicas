"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 16:
Crea una función que meta en una caja de asteriscos la frase 
que le pasemos por parametro
 
Ejemplos:
mostrarTextoCaja('Hola soy Víctor Robles WEB');
 
**********
* Hola   *
* soy    *
* Víctor *
* Robles *
* WEB    *
**********
"""


def mostrarTextoCaja(texto):

    texto = texto.split()
    palabra_mas_larga = max(texto, key=len)

    longitud_palabra_larga = len(palabra_mas_larga)

    longitud_caja = len(palabra_mas_larga) + 4

    print("*" * longitud_caja)

    inicio = "* "

    for palabra in texto:

        longitud_palabra = len(palabra)
        cantidad_espacios = " " * (longitud_palabra_larga - longitud_palabra)
        print(f"{inicio}{palabra}{cantidad_espacios} *")

    print("*" * longitud_caja)


    


mostrarTextoCaja('Hola soy Victor Robles WEB')
mostrarTextoCaja('Hola soy Kakaroto el mejor sayayin')





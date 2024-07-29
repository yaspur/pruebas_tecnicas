"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 4:
Crea el juego del ahorcado.
El usuario tendrá que ir adivinando y descubriendo las letras de una palabra 
secreta, y tendrá 5 intentos (un intento por extremidad del cuerpo humano).
 
Utiliza el método de entrada de datos habitual de tu lenguaje,
en el caso de JS, usaremos la función prompt.
 
Ejemplo:
juegoDelAhorcado('victor');  
 
Salida:
Adivina la letra: i
La palabra es: _i___
Te quedan 5 intentos
"""

def juegoDelAhorcado(palabra):

    letras_palabra = [letra.lower() for letra in palabra]

    intentos = 5

    letras_adivinadas = ['_' for _ in palabra]

    print(f"La palabra a adivinar es: {letras_adivinadas}")

    while intentos > 0:
        letra = input("Adivina la letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Solo se permiten letras.")
            continue
            
        if letra in letras_palabra:
            posiciones = [i for i, l in enumerate(letras_palabra) if l == letra]
            for pos in posiciones:
                letras_adivinadas[pos] = letra
            # posicion = letras_palabra.index(letra)
            # letras_adivinadas[posicion] = letra
            print(f"Correcta! La letra {letra} está en la palabra, está en las posiciones: {', '.join(str(p + 1) for p in posiciones)}")
            palabra_adivinada = "".join(letras_adivinadas)
            print(f"La palabra es: {palabra_adivinada}")
        else:
            intentos -= 1
            print(f"letra incorrecta, te quedan {intentos} intentos")

        if '_' not in letras_adivinadas:
            break

    if intentos > 0:
        print("Haz ganado! se acabo el juego")
    else:
        print("Se acabaron los intentos, perdiste")
        print(f"La palabra es: {palabra}")

juegoDelAhorcado('Yasidi')
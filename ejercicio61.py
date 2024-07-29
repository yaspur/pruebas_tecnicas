"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 61:
Dado una cadena de números, devuelve todas las combinaciones de letras posibles 
que el número podría representar.
 
Aqui tienes un mapeo de dígitos a letras 
(como en los botones de un teléfono).
 
    const mapeo = [
      ' ', // 0
      '', // 1
      'abc', // 2
      'def', // 3
      'ghi', // 4
      'jkl', // 5
      'mno', // 6
      'pqrs', // 7
      'tuv', // 8
      'wxyz' // 9
    ];
 
Ejemplos:
combinacionesLetras("23")
 
Devuelve:
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""


def combinaciones_letras(numero):
    """
    Devuelve todas las combinaciones de letras posibles que un número podría representar.

    Args:
        numero (str): La cadena de números.

    Returns:
        list: Lista de cadenas que representan las combinaciones de letras.
    """

    mapa_digitos_a_letras = [
        ' ',  # 0
        '',  # 1
        'abc',  # 2
        'def',  # 3
        'ghi',  # 4
        'jkl',  # 5
        'mno',  # 6
        'pqrs',  # 7
        'tuv',  # 8
        'wxyz'  # 9
    ]

    def backtrack(numero, indice, cadena):
        if indice == len(numero):
            combinaciones_letras.append(cadena)
            return

        digito = numero[indice]
        letras = mapa_digitos_a_letras[int(digito)]

        for letra in letras:
            nueva_cadena = cadena + letra
            backtrack(numero, indice + 1, nueva_cadena)

    combinaciones_letras = []
    backtrack(numero, 0, "")
    return combinaciones_letras

        
# Ejemplo de uso
numero = "234"
combinaciones = combinaciones_letras(numero)
print(combinaciones)
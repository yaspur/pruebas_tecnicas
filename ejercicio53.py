"""
/*
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 53:
Crea una función para encontrar la longitud del mayor
subconjunto de caracteres que no se repiten.
 
Ejemplos:
encontrarSubcadenaSinRepetir("abcabcbb")  // abc, 3
encontrarSubcadenaSinRepetir("bbbbb")     // b, 1
encontrarSubcadenaSinRepetir("pwwkew")    // wke, 3
*/
"""

def encontrar_subcadenas_sin_repetir(texto: str):
    
    subcadena_sin_repetir = ""
    
    subcadena_actual = ""

    for letra in texto:
        
        if letra in subcadena_actual:
            subcadena_actual = ""
        
        subcadena_actual += letra
        
        if len(subcadena_actual) > len(subcadena_sin_repetir):
            subcadena_sin_repetir = subcadena_actual
            
    return subcadena_sin_repetir, len(subcadena_sin_repetir)

print(encontrar_subcadenas_sin_repetir("abcabcbb"))
print(encontrar_subcadenas_sin_repetir("bbbbb"))
print(encontrar_subcadenas_sin_repetir("pwwkew"))
        
        
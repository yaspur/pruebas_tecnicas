"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 13:
Crea una funcion que calcule el area de un cuadrado, un rectangulo o un triangulo
 
Ejemplos:
calcularAreaPoligono({ tipo: 'triangulo', base: 6, altura: 9 }); 
 
Devuelve: 27
 
"""

def calcularAreaPoligono(datosFigura):

    figura = datosFigura["tipo"].lower()

    if figura == "triangulo":
        base = datosFigura["base"]
        altura = datosFigura["altura"]
        return (base * altura) / 2
    
    elif figura == "cuadrado":
        lado = datosFigura["lado"]
        return lado * lado
    
    elif figura == "rectangulo":
        base = datosFigura["base"]
        altura = datosFigura["altura"]
        return base * altura
    
    else:
        return "Introduzca una figura de tipo cuadrado, rectangulo o triangulo"

print(calcularAreaPoligono({
    "tipo": "triangulo",
    "base": 6,
    "altura": 9
}))

print(calcularAreaPoligono({
    "tipo": "cuadrado",
    "lado": 2
}))
"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal.
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 2:
Dada una ruta absoluta de un archivo (de un sistema linux o basado en unix)
crear una función que la simplifique
 
Ejemplo:
simplificarRuta("/home/");             // Salida: /home
simplificarRuta("/x/./y/../../z/");    // Salida: /z
simplificarRuta("/../");               // Salida: /
simplificarRuta("/home//pruebas/");    // Salida: /home/pruebas
"""

def simplificarRuta(ruta: str):

    pila = []

    partes = ruta.split("/")

    for parte in partes:
        if(parte == "..") and len(pila) >= 1:
            pila.pop()
        elif parte != "." and parte != "" and parte != "..":
            pila.append(parte)

    return "/" + "/".join(pila)

print(simplificarRuta("/home/")) 
print(simplificarRuta("/x/./y/../../z/")) 
print(simplificarRuta("/../"))
print(simplificarRuta("/home//pruebas/")) 
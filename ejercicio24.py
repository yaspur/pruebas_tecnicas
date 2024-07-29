"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 24:
Crea una función a la cual le pasemos un array de nombres de archivo
y nos devuelva un array con esos mismos archivos, pero si hay alguno
duplicado debe estar númerado con un (numero de repeticiones)
como hacen los sistemas operativos.
 
Ejemplos:
renombrarArchivos(["nombre", "apellido", "nombre", "nombre"]);
 
Devuelve: 
[ 'nombre', 'apellido', 'nombre(1)', 'nombre(2)' ]
"""

def renombrarArchivos(archivos):

    cantidad_archivos = {}
    lista_archivos = []

    for archivo in archivos:

        if archivo in cantidad_archivos:
            cantidad_archivos[archivo] += 1
            nombre_archivo = f"{archivo}({cantidad_archivos[archivo] - 1})"
            lista_archivos.append(nombre_archivo)
        else:
            cantidad_archivos[archivo] = 1
            lista_archivos.append(archivo)

    return lista_archivos

print(renombrarArchivos(["nombre", "nombre", "apellido", "nombre", "nombre"]))








"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 25:
Crea una función a la cual le pasemos un array de nombres de archivo
y nos devuelva un array con esos mismos archivos, pero si hay alguno
duplicado debe estar númerado con un (numero de repeticiones)
como hacen los sistemas operativos.
 
Ejemplos:
renombrarArchivos(["nombre.jpg", "apellido.doc", "nombre.png", "nombre.png", "nombre.jpg", "nombre.jpg"]);
 
Devuelve: 
[ 'nombre.jpg', 'apellido.doc', 'nombre.png', 'nombre(1).png', 'nombre(1).jpg', 'nombre(2).jpg']
"""

def renombrarArchivos(archivos):

    cantidad_archivos = {}
    lista_archivos = []

    for archivo in archivos:

        if archivo in cantidad_archivos:
            cantidad_archivos[archivo] += 1
            nombre = archivo.split(".")[0]
            extension = archivo.split(".")[1]
            nombre_archivo = f"{nombre}({cantidad_archivos[archivo] - 1}).{extension}"
            lista_archivos.append(nombre_archivo)
        else:
            cantidad_archivos[archivo] = 1
            lista_archivos.append(archivo)

    return lista_archivos

print(renombrarArchivos(['nombre.jpg', 'apellido.doc', 'nombre.png', 'nombre.png', 'nombre.jpg', 'nombre.jpg']))
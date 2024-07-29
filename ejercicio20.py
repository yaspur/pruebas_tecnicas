"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal (salvo excepciones).
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 20:
Crea una función que ordene un array de objetos en base a las propiedades
que le pase por parametro.
 
  const usuarios = [
    { nombre: 'Antonio', edad: 20 },
    { nombre: 'Juan', edad: 23 },
    { nombre: 'Pepe', edad: 12 },
    { nombre: 'Raul', edad: 28 },
    { nombre: 'Paco', edad: 38 },
    { nombre: 'Jason', edad: 56}
  ];
 
 
Ejemplos:
ordenarObjetos(usuarios, "edad");
"""

def ordenar_por_propiedad(usuarios, propiedad):
    return sorted(usuarios, key=lambda x: x[propiedad])

usuarios = [
    { 'nombre': 'Antonio', 'edad': 20 },
    { 'nombre': 'Juan', 'edad': 23 },
    { 'nombre': 'Pepe', 'edad': 12 },
    { 'nombre': 'Raul', 'edad': 28 },
    { 'nombre': 'Paco', 'edad': 38 },
    { 'nombre': 'Jason', 'edad': 56}
]

propiedad_a_ordenar = 'edad'  # Puedes cambiar esto por 'edad' para ordenar por edad

usuarios_ordenados = ordenar_por_propiedad(usuarios, propiedad_a_ordenar)

for usuario in usuarios_ordenados:
    print(usuario)
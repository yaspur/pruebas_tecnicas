"""
Dado un array de objetos de usuarios, con nombre y fecha,
crea una función que los ordene por fecha.
 
[
  {
    nombre: "Juan",
    fecha: new Date(1984, 7, 10),
  },
  {
    nombre: "Paco",
    fecha: new Date(2017, 8, 12),
  },
  {
    nombre: "Pepe",
    fecha: new Date(1991, 12, 6),
  },
]
 
Ejemplos:
ordenarPorFecha(usuarios)
 
Devolver solo nombre
"""

import datetime

usuarios = [
    {
        "nombre": "Juan",
        "fecha": datetime.date(1984, 7, 10),
    },
    {
        "nombre": "Paco",
        "fecha": datetime.date(2017, 8, 12),
    },
    {
        "nombre": "Pepe",
        "fecha": datetime.date(1991, 12, 6),
    },
]

def ordenar_por_fecha(usuarios):
    usuarios_ordenados = sorted(usuarios, key=lambda x: x["fecha"])
    return usuarios_ordenados

usuarios_ordenados = ordenar_por_fecha(usuarios)
nombres_ordenados = [usuario["nombre"] for usuario in usuarios_ordenados]
print(nombres_ordenados)

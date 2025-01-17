"""
Advertencias:
- En español por fines didacticos, en la vida real usa nombres en ingles.
- Test en cada ejercicio, lo veremos al final del curso para ir al grano.
- Ejercicios genéricos, puedes usar cualquier lenguaje.
- Ejercicios nuevos y diferentes a los del Master en Lógica de Programación
- Siempre mostrar el resultado en la consola / terminal.
- Hay muchas soluciones validas para un mismo ejercicio.
 
Enunciado Ejercicio 3:
Dadas dos fechas, crea una función que me proporcione la diferencia de dias
entre ellas
 
Ejemplo:
diferenciaDeDias('Dec 1, 2023', 'Dec 24, 2023');  // Salida: 23
"""
from datetime import datetime

def diferenciaDeDias(fechaUno, fechaDos):

    fecha1_obj = datetime.strptime(fechaUno, "%b %d, %Y").date()
    fecha2_obj = datetime.strptime(fechaDos, "%b %d, %Y").date()

    diferenciaDeDias = abs((fecha1_obj - fecha2_obj).days)
    
    return diferenciaDeDias
    


print(diferenciaDeDias("Jan 1, 2023","Dec 31, 2023"))
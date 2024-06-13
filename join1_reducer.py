#!/usr/bin/env python
import sys

current_show = None  # Programa actual
current_count = 0  # Conteo actual de espectadores
is_abc = False  # Indicador si es un programa de ABC

# Leer cada línea de la entrada estándar
for line in sys.stdin:
    line = line.strip()  # Eliminar cualquier espacio en blanco
    title, value = line.split('\t')  # Dividir la línea en título y valor

    if title != current_show:
        # Si cambiamos de programa, emitir los resultados del programa anterior si es de ABC
        if current_show is not None and is_abc:
            print(f"{current_show} {current_count}")
        current_show = title  # Actualizar el programa actual
        current_count = 0  # Reiniciar el conteo de espectadores
        is_abc = False  # Reiniciar el indicador de ABC

    if value == 'ABC':
        is_abc = True  # Marcar como programa de ABC
    else:
        current_count += int(value)  # Sumar al conteo de espectadores

# No olvidar emitir el último programa si era de ABC
if is_abc:
    print(f"{current_show} {current_count}")

#!/usr/bin/env python
import sys

# Leer cada línea de la entrada estándar
for line in sys.stdin:
    line = line.strip()  # Eliminar cualquier espacio en blanco
    parts = line.split(",")  # Dividir la línea en partes

    if len(parts) != 2:
        continue  # Saltar cualquier línea que no tenga exactamente dos partes

    title, value = parts

    # Verificar si la parte de 'value' es un canal o un número de espectadores
    if value.isdigit():
        # Es un conteo de espectadores, emitir título y conteo de espectadores
        print(f"{title}\t{value}")
    elif value == 'ABC':
        # Es un programa de ABC, emitir título y marcador de canal
        print(f"{title}\tABC")

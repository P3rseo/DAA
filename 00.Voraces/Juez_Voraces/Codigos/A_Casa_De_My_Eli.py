def llenar_habitacion(canddts, idx_talento, capacidad):
    #  Ordenar los candidatos por talento / u. de espacio
    canddts.sort(key=lambda x: x[idx_talento] / x[1], reverse=True)

    espacio_actual = 0.0
    talento_total = 0.0
    elegidos = []
    usados = 0

    for nombre, espacio, t1, t2, t3 in canddts:
        talento = [t1, t2, t3][idx_talento - 2]
        if espacio_actual + espacio <= capacidad:
            espacio_actual += espacio
            talento_total += talento
            elegidos.append(nombre)
            usados += 1
        else:
            resto = capacidad - espacio_actual
            if resto > 0:
                frac = resto / espacio
                talento_total += talento * frac
                espacio_actual += espacio * frac
                elegidos.append(nombre)
                usados += 1
                break

    return talento_total, elegidos, usados

# Lectura de entradas
N = int(input().strip())
candidatos = []
for i in range(N):
    partes = input().strip().split()
    nombre = partes[0]
    e, t1, t2, t3 = map(int, partes[1:])
    candidatos.append([nombre, e, t1, t2, t3])  # Duda para el profe. [] o () dentro.

capacidad = list(map(int, input().strip().split()))

# Proceso de impresion
for i, cap in enumerate(capacidad):
    total, nombres, usados = llenar_habitacion(candidatos, i + 2, cap)
    print(f"HABITACION {i}: {total:.2f}")
    for n in nombres:
        print(n)
    del candidatos[:usados]
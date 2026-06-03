def seduccion(c, m, tentadores):
    if c == "beauty":
        tentadores.sort(key=lambda x: x[1] / x[4], reverse=True)
        index = 0
    elif c == "intelligence":
        tentadores.sort(key=lambda x: x[2] / x[4], reverse=True)
        index = 1
    elif c == "kindness":
        tentadores.sort(key=lambda x: x[3] / x[4], reverse=True)
        index = 2
    else:
        print("Error en la entrada de c\n")
        return 1

    habilidad_total = 0.0
    tiempo_actual = 0.0
    seleccionados = []

    for nombre, h1, h2, h3, t in tentadores:
        habilidad = [h1, h2, h3][index]
        if tiempo_actual + t <= m:
            tiempo_actual += t
            habilidad_total += habilidad
            seleccionados.append(nombre)
        else:
            resto = m - tiempo_actual
            if resto > 0:
                frac = resto / t
                tiempo_actual += t * frac
                habilidad_total += habilidad * frac
                seleccionados.append(nombre)
                break

    return seleccionados, habilidad_total


# --- LECTURA DE ENTRADAS ---
N = int(input().strip())  # Numero de concursantes
concustantes = []

for _ in range(N):
    C = input().strip()  # Cualidad que mas valora ese concursante
    M = int(input().strip())  # Tiempo maximo que le queda en el programa
    T = int(input().strip())  # Numero de posibles parejas para el concursante

    tentadores = []
    for j in range(T):
        partes = input().strip().split()
        nombre = partes[0]
        b, i, k, t = map(int, partes[1:])
        tentadores.append((nombre, b, i, k, t))

    concustantes.append((C, M, tentadores))

# --- PROCESO DE IMPRESION ---
for concursante in concustantes:
    c, m, t, tentadores = concursante
    personas, habilidad = seduccion(c, m, tentadores)
    print(" ".join(personas))
    print(f"{habilidad:.2f}")


"""
print(N)
for concustante in concustantes:
    c, m, t, tentadores = concustante
    print(c)
    print(m)
    print(t)
    for tentador in tentadores:
        print(tentador)
"""
def llenar_equipo(candidatos, perfil, salario_maximo):
    if perfil == 0:
        candidatos.sort(key=lambda x: x[1] / x[4], reverse=True)
    elif perfil == 1:
        candidatos.sort(key=lambda x: x[2] / x[4], reverse=True)
    elif perfil == 2:
        candidatos.sort(key=lambda x: x[3] / x[4], reverse=True)
    else:
        print("Error al introducir el perfil\n")
        return 1

    presupuesto_actual = 0.0
    habilidad_total = 0.0
    seleccionados = []

    for nombre, h1, h2, h3, s in candidatos:
        habilidad = [h1, h2, h3][perfil]
        if presupuesto_actual + s <= salario_maximo:
            presupuesto_actual += s
            habilidad_total += habilidad
            seleccionados.append(nombre)
        else:
            resto = salario_maximo - presupuesto_actual
            if resto > 0:
                frac = resto / s
                presupuesto_actual += s * frac
                habilidad_total += habilidad * frac
                seleccionados.append(nombre)
                break

    return habilidad_total, seleccionados

#  --- LECTURA DE ENTRADAS ---
N = int(input().strip())  # Numero de recultas disponibles

candidatos = []
for _ in range(N):
    partes = input().strip().split()
    nombre = partes[0]
    a, s, i, g = map(int, partes[1:])
    candidatos.append([nombre, a, s, i, g])

P = int(input().strip())  # Numero de equipos que queremos

equipos = []
for _ in range(P):
    x, m = map(int, input().strip().split())
    equipos.append([x, m])

# --- PROCESO DE IMPRESION
for equipo in equipos:
    habilidad, nombres = llenar_equipo(candidatos, equipo[0], equipo[1])
    print(f"{habilidad:.2f}")
    print(f" ".join(nombres))
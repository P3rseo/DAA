# --- FUNCTIONS --- 
def mochila(reclutas, perfil, presupuestoMaximo):
    if perfil == 0:
        reclutas.sort(key=lambda x: x[1] / x[4], reverse = True)
    elif perfil == 1:
        reclutas.sort(key=lambda x: x[2] / x[4], reverse = True)
    elif perfil == 2:
        reclutas.sort(key=lambda x: x[3] / x[4], reverse = True)
    else:
        print("El perfil debe ser una de estas opciones: [0, 1, 2]")

    presupuestoActual = 0.0
    habilidadTotal = 0.0
    nombreReclutas = []

    for nombre, pen, crayon, pencil, salario in reclutas:
        habilidad = [pen, crayon, pencil][perfil]
        if presupuestoActual + salario <= presupuestoMaximo:
            presupuestoActual += salario
            habilidadTotal += habilidad
            nombreReclutas.append(nombre)
        else:
            resto = presupuestoMaximo - presupuestoActual
            if resto > 0:
                fraccion = resto / salario
                habilidadTotal += habilidad * fraccion
                presupuestoActual += presupuesto * fraccion
                nombreReclutas.append(nombre)
                break

    return habilidadTotal, nombreReclutas



# --- INPUTS ---
numReclutas = int(input().strip())

reclutas = []
for reculta in range(numReclutas):
    partes = input().strip().split()
    nombre = partes[0]
    pen, crayon, pencil, salario = map(int, partes[1:])
    reclutas.append([nombre, pen, crayon, pencil, salario])

numEquipos = int(input().strip())

equipos = []
for equipo in range(numEquipos):
    perfil, presupuesto = map(int, input().strip().split())
    equipos.append([perfil, presupuesto])

# --- OUTPUT --- 
for perfil, presupuesto in equipos:
    habilidadTotal, nombreReclutas = mochila(reclutas, perfil, presupuesto)
    print(f"{habilidadTotal:.2f}")
    print(f" ".join(nombreReclutas))


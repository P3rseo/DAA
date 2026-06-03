
def maximizar_tentacion(cualidad, tiempoMax, candidatos):
        
    cualidadSeleccionada = -1
    if cualidad == "beauty":
        candidatos.sort(key=lambda x: x[1] / x[4], reverse=True)
        cualidadSeleccionada = 0
    if cualidad == "intelligence":
        candidatos.sort(key=lambda x: x[2] / x[4], reverse=True)
        cualidadSeleccionada = 1
    if cualidad == "kindness":
        candidatos.sort(key=lambda x: x[3] / x[4], reverse=True)
        cualidadSeleccionada = 2
    
    tiempoActual = 0.0
    tentacionTotal = 0.0
    nombres = []

    for nombre, b, i, k, t in candidatos:
        seleccionCualidad = [b, i, k][cualidadSeleccionada]
        if tiempoActual + t <= tiempoMax:
            tiempoActual += t
            tentacionTotal += seleccionCualidad
            nombres.append(nombre)
        else:
            resto = tiempoMax - tiempoActual
            if resto > 0:
                fraccion = resto / t
                tiempoActual += t * fraccion
                tentacionTotal += seleccionCualidad * fraccion
                nombres.append(nombre)
                break
    return nombres, tentacionTotal


numConcursantes = int(input().strip())

concursantes = []
for concursante in range(numConcursantes):
    cualidad = input().strip()
    tiempoMaximoRestante = int(input().strip())
    posiblesParejas = int(input().strip())

    posiblesCandidatos = []
    for candidatos in range(posiblesParejas):
        partes = input().strip().split()
        nombre = partes[0]
        b, i, k, tiempoSeduccion = map(int, partes[1:])
        posiblesCandidatos.append([nombre, b, i, k, tiempoSeduccion])
    concursantes.append([cualidad, tiempoMaximoRestante, posiblesCandidatos])

for cualidad, tiempoMaximoRestante, posiblesCandidatos in concursantes:
    nombres, tentacionTotal = maximizar_tentacion(cualidad, tiempoMaximoRestante, posiblesCandidatos)
    print(" ".join(nombres))
    print(f"{tentacionTotal:.2f}")

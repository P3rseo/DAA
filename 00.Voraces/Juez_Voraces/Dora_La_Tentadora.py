def calcularDiaMax(tentadores):
    diaMax = -1
    for tentador in tentadores:
        nombre, capMax, tentacion = tentador
        if capMax > diaMax:
            diaMax = capMax
    return diaMax

def scheduling(tentadores, diaMax):
    tentadores.sort(key=lambda x: x[2], reverse=True)
    seleccionados = [None] * (diaMax + 1)
    for tentador in tentadores:
        dia = tentador[1]
        encontrado = False
        while dia >= 0 and not encontrado:
            if seleccionados[dia] is None:
                seleccionados[dia] = tentador
                encontrado = True
            dia -= 1
    return seleccionados

# --- INPUTS ---
numTentadores = int(input().strip())
tentadores = []
for i in range(numTentadores):
    partes = input().strip().split()
    nombre = partes[0]
    capMax, nivelTentacion = map(int, partes[1:])
    tentadores.append([nombre, capMax, nivelTentacion])

diaMax = calcularDiaMax(tentadores)

# --- OUTPUTS ---
seleccionados = scheduling(tentadores, diaMax)
for i, seleccionado in enumerate(seleccionados):
    if seleccionado is None:
        print(f"DIA {i}: SIN TENTADOR")
    else:
        print(f"DIA {i}: {seleccionado[0]}, LE SOBRAN {seleccionado[1] - i} DIAS")
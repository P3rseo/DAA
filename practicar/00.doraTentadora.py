def maximizar_tentación(tentadores, diaMax):
    tentadores.sort(key=lambda x: x[2], reverse = True)
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


numTentadores = int(input().strip())

diaMax = -1
tentadores = []

for tentador in range(numTentadores):
    partes = input().strip().split()
    nombre = partes[0]
    capMax = int(partes[1])
    nivelTentacion = int(partes[2])
    if capMax > diaMax:
        diaMax = capMax
    tentadores.append([nombre, capMax, nivelTentacion])

seleccionados = maximizar_tentación(tentadores, diaMax)
for i, seleccionado in enumerate(seleccionados):
    if seleccionado is None:
        print(f"DIA {i}: SIN TENTADOR")
    else:
        print(f"DIA {i}: {seleccionado[0]}, LE SOBRAN {seleccionado[1] - i} DIAS")

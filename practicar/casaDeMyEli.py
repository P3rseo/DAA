def mochila(concursantes, capacidad, idxTalento):
    # Ordenamos los concursantes por talento
    concursantes.sort(key=lambda x: x[idxTalento] / x[1], reverse = True)
    talentoTotal = 0
    espacioActual = 0
    usados = 0
    nombres = []

    for concursante in concursantes:
        nombre,espacio,t1,t2,t3 = concursante
        talento = [t1,t2,t3][idxTalento - 2]

        if espacioActual + espacio <= capacidad:
            espacioActual += espacio
            talentoTotal += talento
            usados += 1
            nombres.append(nombre)
        else:
            resto = capacidad - espacioActual
            if resto > 0:
                fraccion = resto / espacio
                talentoTotal += talento * fraccion
                espacioActual +=  espacio * fraccion
                usados += 1
                nombres.append(nombre)
                break
    return talentoTotal, nombres, usados


# Número de concursantes
numConcursantes = int(input().strip())

# Talento y espacio de los concursantes
concursantes = []
for _ in range(numConcursantes):
    partes = input().strip().split()
    nombre = partes[0]
    espacio, talento1, talento2, talento3 = map(int, partes[1:])
    concursantes.append((nombre, espacio, talento1, talento2, talento3))

# Espacio de las habitaciones
capacidadHabitaciones = list(map(int, input().strip().split()))


for i,capacidad in enumerate(capacidadHabitaciones):
    # Aplicamos mochila a cada habitación
    talentoTotal, nombreConcursantes, usados = mochila(concursantes, capacidad, i+2)
    
    # Imprimir solución
    print(f"HABITACION {i}: {talentoTotal:.2f}")
    for nombre in nombreConcursantes:
        print(nombre) 

    # Eliminamos los concursantes que ya hemos seleccionado
    del concursantes[:usados]


def busquedaBinaria(lista, buscado, inferior, superior, tiempo):
    if inferior > superior:
        return -1, tiempo
    else:
        mitad = (superior + inferior) // 2

    if lista[mitad][0] == buscado:
        return mitad, tiempo-1
    if buscado < lista[0][0]:
        return -1, tiempo
    if buscado > lista[len(lista)-1][0]:
        return -1, tiempo
    elif buscado < lista[mitad][0]:
        return busquedaBinaria(lista, buscado, inferior, mitad-1, tiempo-1)
    else:
        return busquedaBinaria(lista, buscado, mitad+1, superior, tiempo-1)


# --- INPTUS ---
numJugadores = int(input().strip())
jugadores = []

for i in range(numJugadores):
    partes = input().strip().split()
    dorsal = int(partes[0])
    nombre = partes[1]
    jugadores.append((dorsal, nombre))

numJugadoresDora = int(input().strip())
enjuego = []

for i in range(numJugadoresDora):
    dorsal, tiempo = map(int, input().strip().split())
    enjuego.append((dorsal, tiempo))

for dorsal, tiempo in enjuego:
    pos, tiempoTarda = busquedaBinaria(jugadores, dorsal, 0, len(jugadores)-1, tiempo)
    if pos == -1 or tiempoTarda < 0:
        print(f"Nosequien")
    else:
        print(f"{jugadores[pos][1]}")



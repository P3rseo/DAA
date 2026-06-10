def binary_search(lista, buscado, inferior, superior, tiempoMax):
    if inferior > superior or tiempoMax <= 0:
        return -1
    
    mitad = (inferior + superior) // 2

    if lista[mitad][0] == buscado:
        return mitad
    elif buscado < lista[mitad][0]:
        return binary_search(lista, buscado, inferior, mitad-1, tiempoMax-1)
    else:
        return binary_search(lista, buscado, mitad+1, superior, tiempoMax-1)
    

numJugadores = int(input().strip())

jugadores = []
for _ in range(numJugadores):
    partes = input().strip().split()
    dorsal = int(partes[0])
    nombre = partes[1]
    jugadores.append([dorsal, nombre])

numJugadoresDecirDora = int(input().strip())

jugadoresDecirDora = []
for _ in range(numJugadoresDecirDora):
    dorsalJugador, tiempo = map(int, input().strip().split())
    jugadoresDecirDora.append([dorsalJugador, tiempo])


for dorsal, tiempo in jugadoresDecirDora:
    pos = binary_search(jugadores, dorsal, 0, len(jugadores)-1, tiempo)
    if pos == -1:
        print("Nosequien")
    else:
        print(jugadores[pos][1])




"""
print(numJugadores)
for jugador in jugadores:
    print(jugador)
print(numJugadoresDecirDora)
for jugadorDora in jugadoresDecirDora:
    print(jugadorDora)
"""



numCiudades, numCarreteras = map(int, input().strip().split())

conexiones = [[] for _ in range(numCiudades)]

mediaFuerzasDesplegadas = 0

for _ in range(numCarreteras):
    c1, c2, fSeguridad = map(int, input().strip().split())
    mediaFuerzasDesplegadas += fSeguridad
    conexiones[c1].append((c2, fSeguridad))
    conexiones[c2].append((c1, fSeguridad))

mediaFuerzasDesplegadas /= numCarreteras

distancias, precedencias = kruskal
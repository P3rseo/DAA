import math


def distancia_euclidea(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def fuerza_bruta(puntos_x):
    n = len(puntos_x)
    min_distancia = 0x3f3f3f3f  # float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            d = distancia_euclidea(puntos_x[i], puntos_x[j])
            min_distancia = min(d, min_distancia)

    return min_distancia


def combinar(franja, d):
    min_distancia = d
    for i in range(len(franja)):
        for j in range(i+1, len(franja)):
            if franja[j][1] - franja[i][1] < min_distancia:
                distancia = distancia_euclidea(franja[i], franja[j])
                min_distancia = min(distancia, min_distancia)

    return min_distancia


def dyv_puntos_cercanos(puntos_x, puntos_y):
    n = len(puntos_x)
    if n <= 3:
        return fuerza_bruta(puntos_x)
    else:
        mid = n // 2
        puntos_x_i = puntos_x[:mid]
        puntos_x_d = puntos_x[mid:]

        puntos_y_i = []
        puntos_y_d = []

        mid_x = puntos_x[mid][0]

        for p in puntos_y:
            if p[0] <= mid_x:
                puntos_y_i.append(p)
            else:
                puntos_y_d.append(p)

        min_i = dyv_puntos_cercanos(puntos_x_i, puntos_y_i)
        min_d = dyv_puntos_cercanos(puntos_x_d, puntos_y_d)

        d = min(min_i, min_d)

        franja = []
        for p in puntos_y:
            if abs(p[0] - mid_x) < d:
                franja.append(p)

        dist_franja = combinar(franja, d)
        return dist_franja


# --- INPUTS ---
numTiendasAbiertas, costeEnviarMasCercanas = map(int, input().strip().split())

cordTiendas = []
for i in range(numTiendasAbiertas):
    cordX, cordY = map(int, input().strip().split())
    cordTiendas.append((cordX, cordY))

puntos_x = cordTiendas.copy()
puntos_x.sort(key=lambda p: p[0])
puntos_y = cordTiendas.copy()
puntos_y.sort(key=lambda p: p[1])

numQueries = int(input().strip())
queries = []
for i in range(numQueries):
    tienda1, tienda2 = map(int, input().strip().split())
    queries.append((tienda1, tienda2))

distancia_minima = dyv_puntos_cercanos(puntos_x, puntos_y)
print(f"MINIMO: {distancia_minima:.2f}")

factor = costeEnviarMasCercanas / distancia_minima

for tienda1, tienda2 in queries:
    d = distancia_euclidea(cordTiendas[tienda1], cordTiendas[tienda2])
    coste = d * factor
    print(f"{tienda1} -> {tienda2}: {coste:.2f}")

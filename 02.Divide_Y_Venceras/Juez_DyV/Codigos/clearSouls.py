def puntosEn(lista):
    value = 0
    resultado = []

    for elem in lista:
        value += elem
        resultado.append(value)

    return resultado

def binarySearch(lista, puntosEnemigos, buscado, inferior, superior):

    enemigosDerrotados = 0

    if inferior > superior:
        return inferior, puntosEnemigos[superior]

    mitad = (superior + inferior) // 2

    if buscado == lista[mitad]:
        enemigosDerrotados = len(lista[:mitad+1])
        return enemigosDerrotados, puntosEnemigos[mitad]

    if buscado < lista[0]:
        return enemigosDerrotados, 0

    if buscado > lista[len(lista) - 1]:
        enemigosDerrotados = len(lista)
        return enemigosDerrotados, puntosEnemigos[len(puntosEnemigos)-1]

    elif buscado < lista[mitad]:
        return binarySearch(lista, puntosEnemigos, buscado, inferior, mitad-1)

    else:
        return binarySearch(lista, puntosEnemigos, buscado, mitad+1, superior)


# --- INPUTS ---
numEnemigos = int(input().strip())
nivelEnemigos = list(map(int, input().strip().split()))
puntosEnemigos = puntosEn(nivelEnemigos)

numCasosPrueba = int(input().strip())
casosPrueba = []
for caso in range(numCasosPrueba):
    nivelCaballero = int(input().strip())
    casosPrueba.append(nivelCaballero)

# --- OUTPUT ---
for caso in casosPrueba:
    pos, puntos = binarySearch(nivelEnemigos, puntosEnemigos, caso, 0, len(nivelEnemigos))
    print(f"{pos} {puntos}")

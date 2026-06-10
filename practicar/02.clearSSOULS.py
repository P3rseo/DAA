def calcular_puntos(nivelEnemigos):
    sumatorio = 0
    sumNiveles = []
    for nivel in nivelEnemigos:
        sumatorio += nivel
        sumNiveles.append(sumatorio)
    return sumNiveles

def binary_search(lista, buscado, inferior, superior):
    if buscado >= lista[len(lista)-1]:
        return len(lista) - 1
    elif buscado < lista[0]:
        return -1
    elif inferior > superior:
        return superior
    
    mitad = (inferior + superior) // 2
    
    if lista[mitad] == buscado:
        return mitad
    elif buscado < lista[mitad]:
        return binary_search(lista, buscado, inferior, mitad-1)
    else:
        return binary_search(lista, buscado, mitad+1, superior)




numEnemigosOleada = int(input().strip())
enemigos = list(map(int, input().strip().split()))
numCasosPrueba = int(input().strip())
nivelesCasoPrueba = []
for _ in range(numCasosPrueba):
    nivel = int(input().strip())
    nivelesCasoPrueba.append(nivel)

sumatorioNiveles = calcular_puntos(enemigos)

for nivelCaballero in nivelesCasoPrueba:
    pos = binary_search(enemigos, nivelCaballero, 0, len(enemigos)-1)
    if pos != -1:
        print(f"{pos+1} {sumatorioNiveles[pos]}")
    else:
        print("0 0")





"""
print(numEnemigosOleada)
print(*enemigos)
print(numCasosPrueba)
print(*nivelesCasoPrueba)
"""
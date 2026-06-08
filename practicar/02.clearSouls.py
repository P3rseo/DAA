def punosEn(lista):
    valor = 0
    resultado = []
    for nivel in lista:
        valor += nivel
        resultado.append(valor)
    return resultado

def binsearch(lista, buscado, inferior, superior):
    if buscado < lista[0]:
        return -1
    if buscado > lista[len(lista)-1]:
        return len(lista)-1
    if inferior == superior:
        return superior
    
    mitad = (inferior + superior) // 2

    if lista[mitad] == buscado:
        return mitad
    elif buscado < lista[mitad]:
        return binsearch(lista, buscado, inferior, mitad-1)
    else:
        return binsearch(lista, buscado, mitad+1, superior)  


numEnemigos = int(input().strip())
nivelEnemigos = list(map(int, input().strip().split()))
puntosEnemigos = punosEn(nivelEnemigos)
numCasosPrueba = int(input().strip())
casosDePrueba = []
for _ in range(numCasosPrueba):
    casosDePrueba.append(int(input().strip()))

for caso in casosDePrueba:
    posicion = binsearch(nivelEnemigos, caso, 0, numEnemigos-1)
    if posicion != -1:
        print(f"{posicion+1} {puntosEnemigos[posicion]}")
    if posicion == -1:
        print(f"0 0")
    


"""
print(numEnemigos)
print(nivelEnemigos)
print(numCasosPrueba)
print(casosDePrueba)
"""
def binary_search(lista, buscado, inferior, superior):
    if inferior > superior:
        return -1, superior+1
    
    mitad = (inferior + superior) // 2

    if lista[mitad][0] == buscado:
        return lista[mitad][1], mitad
    elif buscado < lista[mitad][0]:
        return binary_search(lista, buscado, inferior, mitad-1)
    else:
        return binary_search(lista, buscado, mitad+1, superior)



numSupermercados = int(input().strip())

supermercados = []
for _ in range(numSupermercados):
    idSuper, numProductos = map(int, input().strip().split())
    supermercados.append([numProductos, idSuper])



supermercados.sort()

numConsultas = int(input().strip())

consultas = []
for _ in range(numConsultas):
    numProductos = int(input().strip())
    consultas.append(numProductos)

for numProductos in consultas:
    exacto, menores = binary_search(supermercados, numProductos, 0, len(supermercados)-1)
    if exacto == -1:
        print(f"NO {menores} {len(supermercados)-menores}")
    else:
        print(f"{exacto} {menores} {len(supermercados)-menores}")
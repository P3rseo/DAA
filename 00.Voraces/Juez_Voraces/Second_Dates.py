def divideCandidates(candidatos, size):
    # Ordenamos los candidatos de menor a mayor
    candidatos.sort(key=lambda x: x[1])

    jovenes = []
    mayores = []

    sumaTotal = sum([edad for nombre, edad in candidatos])
    jovenesSize = sum([edad for nombre, edad in candidatos[:size]])
    mayoresSize = sum([edad for nombre, edad in candidatos[-size:]])

    if abs(sumaTotal - 2 * jovenesSize) > abs(sumaTotal - 2 * mayoresSize):
        for nombre, edad in candidatos[:size]:
            jovenes.append(nombre)
        for nombre, edad in candidatos[size:]:
            mayores.append(nombre)
    else:
        for nombre, edad in candidatos[:size-1]:
            jovenes.append(nombre)
        for nombre, edad in candidatos[size-1:]:
            mayores.append(nombre)

    return jovenes, mayores


#  --- INPUTS ---
N, K = input().strip().split()  # Numero de participantes y Tamanio de uno de los grupos

candidatos = []  # Lista de todos los participantes

for _ in range(int(N)):
    partes = input().strip().split()
    nombre = partes[0]
    edad = int(partes[1])
    candidatos.append([nombre, edad])


#  --- IMPRIMIR RESULTADO ---
menores, mayores = divideCandidates(candidatos, int(K))

print(" ".join(menores))
print(" ".join(mayores))
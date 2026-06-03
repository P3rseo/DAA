# --- FUNCIONES ---
def calcularDiferencia(grupo1, grupo2):
    n1 = 0
    n2 = 0
    for n, edad in grupo1:
        n1 += edad
    for n, edad in grupo2:
        n2 += edad
    return abs(n1-n2)

def separar_grupos(candidatos, s1, s2):
    participantes.sort(key=lambda x: x[1])
    if calcularDiferencia(candidatos[:s1], candidatos[s1:]) >= calcularDiferencia(candidatos[:s2], candidatos[s2:]):
        return candidatos[:s1], candidatos[s1:]
    else:
        return candidatos[:s2], candidatos[s2:]


# --- INPUTS ---
numParticipantes, sizeG1 = map(int, input().strip().split())

participantes = []
for _ in range(numParticipantes):
    partes = input().strip().split()
    nombre = partes[0]
    edad = int(partes[1])
    participantes.append([nombre, edad])

jovenes, noJovenes = separar_grupos(participantes, sizeG1, numParticipantes - sizeG1)
for nombre, edad in jovenes:
    print(nombre, end=" ")
print()
for nombre, edad in noJovenes:
    print(nombre, end=" ")
print()



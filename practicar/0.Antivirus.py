def binary_search(lista, buscado, inferior, superior):
    if inferior > superior:
        return -1
    
    mitad = (inferior + superior) // 2
    
    if lista[mitad][0] == buscado:
        return mitad
    elif lista[mitad][0] > buscado:
        return binary_search(lista, buscado, inferior, mitad-1)
    else:
        return binary_search(lista, buscado, mitad+1, superior)



numMuestras = int(input().strip())
muestras = []
for _ in range(numMuestras):
    partes = input().strip().split()
    hashMuestra = partes[0]
    numLineas = int(partes[1])
    muestras.append([hashMuestra, numLineas])

muestras.sort()

numMuestrasConsultar = int(input().strip())
muestrasConsultar = []
for _ in range(numMuestrasConsultar):
    partes = input().strip().split()
    hashConsultar = partes[0]
    lineasConsultar = int(partes[1])
    muestrasConsultar.append([hashConsultar, lineasConsultar])

totalLineas = 0

for hashConsulta, numLineasConsulta in muestrasConsultar:
    pos = binary_search(muestras, hashConsulta, 0, len(muestras)-1)
    if pos == -1:
        print("NO ENCONTRADO")
        totalLineas += numLineas
    else:
        print("ENCONTRADO")
print(f"{totalLineas}")



"""
a = "bbc4v45h423"
b = "acda34k34qf"
c = "aaakdkfjadfiadfjka"
d = "hakdf4j4h6242kt23j4"
e = "1kj4jtjkk4kjg4"

lista = [a, b, c, d, e]
print(lista)
lista.sort()
print(lista)


if b > a: print("hola")
else: print("NOU")
"""
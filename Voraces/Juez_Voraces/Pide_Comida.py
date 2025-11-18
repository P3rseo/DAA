
#  --- INPUTS ---
C, M = input().strip().split()  # Numero de comensales y Platos que hay en el menu
comensales = []
platos = []  # Lista de platos con su nombre, disfrute y precio
for _ in range(int(M)):
    partes = input().strip().split()
    nombre = partes[0]
    disfrute, precio = map(int, partes[1:])
    platos.append([nombre, disfrute, precio])

for _ in range(int(C)):
    maxPrice = int(input().strip())
    comensales.append(maxPrice)

comilon = comensales[0]


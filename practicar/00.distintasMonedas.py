# --- IMPORTS ---
import math

# --- FUNCIONES --- 
def devolverCambio(monedas, compras, dineroFinal):
    pagos = []
    for tipoMoneda, precioCompra in compras:
        for nombre, cambioAEuro, posiblesCambios in monedas:
            if tipoMoneda == nombre:
                posiblesCambios.sort(reverse = True)
                cambio = []
                precioAux = precioCompra
                for posibleCambio in posiblesCambios:
                    while precioAux >= posibleCambio:
                        precioAux -= posibleCambio
                        cambio.append(posibleCambio)
                pagos.append(cambio)
                dineroFinal += math.ceil(precioCompra * cambioAEuro)
    return dineroFinal, pagos

        
# --- INPUTS ---
dineroInicial = int(input().strip())
cantidadMonedas = int(input().strip())

monedas = []
for moneda in range(cantidadMonedas):
    partes = input().strip().split()
    nombre = partes[0]
    cambioAEuros = float(partes[1])
    posiblesCambios = list(map(int, partes[2:]))
    monedas.append([nombre, cambioAEuros, posiblesCambios])

numComprasAlDia = int(input().strip())

compras = []
for compra in range(numComprasAlDia):
    partes = input().strip().split()
    tipoMoneda = partes[0]
    cantidadGastada = float(partes[1])
    compras.append([tipoMoneda, cantidadGastada])


# --- OUTPUT ---
dineroFinal, pagos = devolverCambio(monedas, compras, dineroInicial)

for i, pago in enumerate(pagos, 1):
    print(f"Pedido {i} paga con", end=" ")
    print(*pago)

print(f"Dinero al final del dia: {dineroFinal}")
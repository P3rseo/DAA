import math


def cajero(cajaInicio, monedas, compras):
    pedidos = []
    for compra in compras:
        nombreCompra, precioCompra = compra
        for tipoMoneda in monedas:
            nombreMoneda, aEuro, posiblesMonedas = tipoMoneda
            if nombreCompra == nombreMoneda:
                monedasDevueltas = []
                precioAPagar = precioCompra
                for moneda in posiblesMonedas:
                    while precioAPagar >= moneda:
                        precioAPagar -= moneda
                        monedasDevueltas.append(moneda)
                pedidos.append(monedasDevueltas)
                precioCompra *= aEuro
                precioCompra = math.ceil(precioCompra)
                cajaInicio += precioCompra

    return cajaInicio, pedidos


#  --- INPUTS ---
dineroInicio = int(input().strip())
cantidadMonedas = int(input().strip())
monedas = []
for _ in range(cantidadMonedas):
    partes = input().strip().split()
    nombre = partes[0]
    cambioEuro = float(partes[1])
    cambios = list(map(int, partes[2:]))
    monedas.append([nombre, cambioEuro, cambios])

P = int(input().strip())
compras = []
for _ in range(P):
    partes = input().strip().split()
    tipoMoneda = partes[0]
    cantidadGasta = int(partes[1])
    compras.append([tipoMoneda, cantidadGasta])

#  --- MOSTRAR RESULTADO ---
cajaFinal, pedidos = cajero(dineroInicio, monedas, compras)
for i, pedido in enumerate(pedidos, 1):
    print(f"Pedido {i} paga con", *pedido, sep=" ")  # Se podria hacer directamente sin sep.
print(f"Dinero al final del dia: {cajaFinal}")
candidatos = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]  # El conjunto de monedas
precioAPagar = 7.88  # Este es el precio que paga el señor y del cual tendremos que devolver el cambio exacto.
solucion = []  # Este sera el conjunto de monedas seleccionadas.

candidatos.sort(reverse=True)  # Necesitamos ordenar la lista en caso de que venga desordenada.

for candidato in candidatos:  # Por cada moneda dentro del conjunto de monedas
    while precioAPagar >= candidato:  # Si el valor es mayor o igual que la moneda
        precioAPagar -= candidato  # Restamos el valor de la moneda al precio a pagar
        """
        OJO CON ESTO! Cuado estoy trabajando con double y float
        No puedo hacer comparaciones directas.
        A veces te da 0.2 y otras 0.2000000000000001. CUIDADO.
        """
        precioAPagar = round(precioAPagar, 2)  # Redondeamos el precio a pagar por los problemas con float y double
        solucion.append(candidato)  # Agregamos el valor de la moneda al conjunto solucion

print(solucion)
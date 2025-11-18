n = 5  # Numero de candidatos
W = 100  # Peso maximo de la mochila
candidatos = [[10, 20, 20/10], [20, 30, 30/20], [30, 66, 66/30], [40, 40, 40/40], [50, 60, 60/50]]  # Candidatos
"""
Otra manera de aniadir el valor entre el peso seria asi:
for candidato in candidatos:
    weight, value = candidato
    candidato.append(value / weight)
"""
print(candidatos)  # Imprimir candidatos antes de ser ordenados
candidatos.sort(key=lambda x: x[2], reverse=True)  # Ordenar los candidatos en funcion de v/w
print(candidatos)  # Imprimir los candidatos ordenados

valorTotal = 0  # Valor inicial
pesoActual = 0  # Peso inicial
seleccionados = []  # Candidatos seleccionados

for candidato in candidatos:
    w, v, r = candidato
    if pesoActual + w <= W:  # Si el pesoActual + el peso del candidato no superan el peso maximo:
        pesoActual += w  # Aniadimos el peso
        valorTotal += v  # Aniadimos el valor
        seleccionados.append(1)  # Aniadimos el candidato entero
    else:  # Si el pesoActual + el peso del candidatos SUPERAN el peso maximo:
        resto = W - pesoActual  # Peso que FALTA para llenar la mochila
        if resto == 0:  # Si este sobrante es negativo significa que ya hemos cubierto el peso maximo.
            seleccionados.append(0)  # Agregamos un 0 a los seleccionados
            continue  # Se salta lo que queda del for y pasa a la siguiente iteracion
        valorTotal += v * (resto / w)  # Aniadimos la parte proporcional del candidato
        pesoActual += w * (resto / w)  # Aniadimos el valor proporcional a lo que entra del candidato
        seleccionados.append(resto / w)  # Aniadimos la parte proporcional del candidato


print(f"\nEl valor total es de: {valorTotal}")
print(f"El peso actual es de: {pesoActual}")
print(f"Los seleccionados son: {seleccionados}")
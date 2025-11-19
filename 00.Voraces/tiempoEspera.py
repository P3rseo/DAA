n = 3  # Numero de candidatos
candidatos = [[1, 5], [2, 10], [3, 3]]  # Lista de candidatos con x: x[0] Num candidato y x[1] tiempo ejecucion.
print(f"El conjunto antes de ser ordenado es {candidatos}")  # Imprimimos los candidatos antes de ser ordenados.
candidatos.sort(key=lambda x: x[1])  # Ordenamos los candidatos en funcion del tiempo de ejecucion. De menos a mas.

solucion = []  # Creamos el conjunto solucion
for candidato in candidatos:
    solucion.append(candidato)  # Introducimos los candidatos ya ordenados en el conjunto solucion.

print(f"El conjunto solucion es: {solucion}")  # Imprimimos el conjunto solucion

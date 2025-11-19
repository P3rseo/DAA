n = 4  # Numero de trabajos
candidatos = [[1, 50, 2], [2, 10, 1], [3, 15, 2], [4, 30, 1]]  # Candidatos: indice, beneficio, fecha tope.
candidatos.sort(key=lambda x: (x[2], -x[1]))  # Ordenamos por fecha tope y beneficio de mayor a menor.
print(candidatos)

limit = candidatos[0][2]  # Ponemos la primera fecha tope existente entre los candidatos
tareas = []  # Lista para guardar las tareas de cada fecha limite
beneficioTotal = 0  # El beneficio total de todas las tareas seleccionadas


for candidato in candidatos:  # Por cada candidato
    if candidato[2] >= limit:  # Si la fecha limite del candidato es mayor o igual a la fecha limite
        beneficioTotal += candidato[1]  # Sumamos el beneficio de la tarea
        tareas.append(candidato[0])  # Aniadimos la tarea a las tareas realizadas
        limit += 1  # Aumentamos el limite en 1

print(f"El beneficio total es {beneficioTotal}")
print(f"Las tareas escogidas son {tareas}")
import copy


def is_sol(lab, r, c):
    return r == len(lab)-1 and c == len(lab[0])-1


def es_mejor(lab, best):
    filas = len(lab)-1
    columnas = len(lab[0])-1
    return lab[filas][columnas] < best[filas][columnas]


def es_factible(lab, new_r, new_c):
    return 0 <= new_r < len(lab) and 0 <= new_c < len(lab[0]) and lab[new_r][new_c] == 0

def laberinto_bt(lab, best, r, c, k):
    if is_sol(lab, r, c):
        if es_mejor(lab, best):
            best = copy.deepcopy(lab)
        else:
            direcciones = [(0,1), (1,0), (0,-1), (-1,0)]
            for direccion in direcciones:
                new_fila = r + direccion[0]
                new_columna = c + direccion[1]
                if es_factible(lab, new_fila, new_columna):
                    lab[new_fila][new_columna] = k
                    best = laberinto_bt(lab, best, new_fila, new_columna, k)
                    lab[new_fila][new_columna] = 0
    return best

# LABERINTO QUE NO TENGO COPIADO.
lab = [[],[]]
k = 1
lab[0][0] = k
best = copy.deepcopy(lab) # Te crea una copia de lo que le paso como parametro. lab.copy esta como rraaaro.

laberinto_bt(lab, best, 0, 0, k+1)


















# MODIFICACIONES SOBRE ESTE EJERCICIO
"""
- ENTRADA Y SALIDA MODIFICADA. DONDE YO QUIERA
"""
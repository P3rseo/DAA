# Fallos a tener en cuenta
## BBDoor
- map(int, input().strip().split())
- Ojo con el .sort()!!. Se me ha olvidad usar el reverse=True para ordenar de mayor a menor.
- En el resto:
    - resto = CapMax - CapActual
    - if resto > 0:
        - fracc = resto / Cap
        - capActual += cap * fracc
        - habTotal += hab * fracc
        - break
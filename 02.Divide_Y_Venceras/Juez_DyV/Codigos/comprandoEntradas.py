def merge(left, right, v):
  l = 0
  r = 0
  i = 0
  inv = 0

  while l < len(left) and r < len(right):
    if left[l] <= right[r]:
      v[i] = left[l]
      l += 1
    else:
      v[i] = right[r]
      r += 1
      inv += (len(left) - l)
    i += 1

  if l < len(left):
    v[i:] = left[l:]
  else:
    v[i:] = right[r:]

  return inv

def merge_sort(v):
  if len(v) == 1:
    return 0

  mid = len(v) // 2
  left = v[:mid]
  right = v[mid:]

  inv = merge_sort(left)
  inv += merge_sort(right)
  inv += merge(left, right, v)
  return inv


# --- INPUT ---
numPersonasCola, numEntradas = map(int, input().strip().split())
cola = list(map(int, input().strip().split()))

pares = merge_sort(cola)
print(pares)
print(*cola[:numEntradas])

c,m=map(int,input().strip().split())
platos=[]
for _ in range(m):
    n,b,p=input().strip().split()
    platos.append([n,int(b),int(p)])
presu=[]
for _ in range(c):
    presu.append(int(input().strip()))

platos.sort(key=lambda x:x[1]/x[2])

Come=0
disfr=0

for i in range(c):
    presu_comensal = presu.pop()
    platoscopy = platos.copy()
    while presu_comensal > 0 and platoscopy:
        nombre,disfrute, precio = platoscopy.pop()
        if presu_comensal >= precio:
            presu_comensal -= precio
            disfr += disfrute
            if not presu:
                Come += disfrute
        else:
            disfr += (presu_comensal/precio)*disfrute
            if not presu:
                Come += (presu_comensal/precio)*disfrute
            presu_comensal = 0


sin_pagar = disfr-Come
print(f"{sin_pagar:.2f}")



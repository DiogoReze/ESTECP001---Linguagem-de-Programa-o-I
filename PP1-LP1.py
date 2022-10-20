n = int(input())

a = []
for i in range(n):
    aux = []
    for j in range(n):
        aux.append(0.0)
    a.append(aux)

#print(a)

for i in range(n):
    for j in range(n):
        if j > i:
            a[i][j] = float(input())
            a[j][i] = a[i][j]

#for i in range(n):
#    print(a[i][:])            
        
n = int(input())

cid = []
for i in range(n):
    if i == 0:
        cid.append(int(input()))
    else:
        cid.append(int(input()))

distPerc = []
for i in range(n-1):
    distPerc.append(cid[i])
    distPerc.append(cid[i+1])
    #print(cid[i],cid[i+1])

distPerc.append(cid[-1])
distPerc.append(cid[0])
#print(cid[-1],cid[0])
#print('\n\n',distPerc)

dist = 0.0
for i in range(0,len(distPerc),2):
    #print(distPerc[i],distPerc[i+1])
    dist = dist + a[distPerc[i]-1][distPerc[i+1]-1]

#print(dist)    

vDiesel = float(input())
cons = 3.0 
custoTotal = (dist / cons) * vDiesel
print('R$ {:.2f}'.format(custoTotal))

        

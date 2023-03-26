K=input().split()
V=input().split()
v="".join(V)
V=list(map(int,V))
v=v.find(str(min(V)))

dictx={}
for count in range(len(K)):
  dictx[K[count]]=V[count]

print(dictx)
print(K[v])

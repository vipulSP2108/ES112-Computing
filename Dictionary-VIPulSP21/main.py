listx=input().split()

dictx={}
for count in range(len(listx)):
  dictx[listx[count]]=len(listx[count])

print(dictx)

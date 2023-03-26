rotate=int(input())
num_places=int(input())
listx=input().split(",")
listx=list(map(int,listx))

if rotate==1:
  count=0
  while count<num_places:
    new=listx[len(listx)-1]
    listx.insert(0,new)
    listx.pop()
    count=count+1
    
elif rotate==-1:
  count=0
  while count<num_places:
    new=listx[len(listx)-1]
    listx.append(listx[0])
    listx.remove(listx[0])
    count=count+1
  
listx=list(map(str,listx))
print(",".join(listx))

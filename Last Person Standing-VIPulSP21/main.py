# k=int(input())
# listx=input().split(",")
# i=k-1
# while len(listx)!=1:
#   listx.pop(i)
#   i=(i+(k-1))%len(listx)
# print(listx[0])

k=int(input())
listx=input().split(",")
while len(listx)>=k:
  if len(listx)==1:
    break
  listx=listx[k:]+listx[:k-1]

if len(listx)==1:
  print(listx[0])
else:
  count=0  
  while listx!=[]:
    while len(listx)<k :
      listx.append(listx[count])
      count=count+1
    last=listx[len(listx)-1]
    listx.remove(last)
    listx.remove(last)
    num=0
    while num<=len(listx)-1:
      if listx[num]==listx[0]:
        if num==len(listx)-1:
          print(listx[num])
          listx=[]
          break
        num=num+1
        continue
      else:
        count=0
        break

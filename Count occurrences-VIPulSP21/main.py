i=int(input())
listx=[]
for n in range(i):
  listx.append(input())

listz=[]
n=1
count=0
while count==0:
  n=1
  if len(listx)!=0:
    a=listx[count-n]
    count1=0
    while count1<len(listx):
      if a==listx[count1]:
        n=n+1
        listx.remove(a)
        count1=0
      else:
        n=n
        count1=count1+1
    n=n-1
    listz.append(n)
  else:
    count=count+1

listz.sort()
print(len(listz))
count=len(listz)-1
while count>=0:
  print(listz[count],end=" ")
  count=count-1

a= int(input())
b= int(input())
for i in range(a,b+1):
  
  if i==1:
    count=1
  else:
    q=2
    count=0
    while q < i:
      if i%q==0:
        count=count+1
        break
      else:
        count=count
      q=q+1
    if count==0:
      print(q,end=" ")

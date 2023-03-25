listx=input().split()
q=0
count=0
for q in range(len(listx)):
  new=listx[q+1:]
  for i in new:
    if i==listx[q]:
      count=count+1
if count==0:
  print("Good")
else:
  print("Not good")

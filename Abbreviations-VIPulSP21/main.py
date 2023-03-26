def Abbrev(a):
  listx=a.split(" ")
  first=listx[0][0]
  secound=listx[1][0]
  last=listx[2]
  return first+". "+secound+". "+last

result=Abbrev(input())
print(result)

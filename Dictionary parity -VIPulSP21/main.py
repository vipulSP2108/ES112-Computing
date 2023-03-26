i=int(input())
dictx={}
for item in range(i):
  num=int(input())
  if num%2==0:
    value="Even"
  else:
    value="Odd"
  dictx[num]=value

print(dictx)
